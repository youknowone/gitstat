#!/usr/bin/python

import os.path
ROOT_PATH = os.path.dirname(__file__)
if not ROOT_PATH:
    ROOT_PATH = './'
else:
    ROOT_PATH += '/'

import sys
import math
import datetime
import re
import ranking
import jinja2

from settings import *

def lpath(path):
    return ROOT_PATH + path

def lopen(path, mode='r'):
    return open(lpath(path), mode)

template_data = lopen(TEMPLATE_FILE).read()
template = jinja2.Template(template_data)

if INPUT_FILE:
    infile = lopen(INPUT_FILE)
else:
    infile = sys.stdin

data = '\n' + infile.read()

class Author(object):
    dictionary = {}

    def __init__(self, email, name=None):
        self.emails = [email]
        self.names = [name] if name else []
        self.commits = []

    def __repr__(self):
        return u"<Author('{0}',{1})>".format(self.email, self.names)

    @property
    def email(self):
        return self.emails[0]

    @property
    def name(self):
        namelen = len(self.names)
        if namelen == 1:
            return self.names[0]
        elif namelen == 0:
            return '<None>'
        else:
            return self.names[0] + u' and {0} other names'.format(namelen - 1)

    @property
    def commit_impact(self):
        return round(math.log(len(self.commits)), 2)

    @property
    def email_name(self):
        return self.email.split('@')[0]

    @property
    def safe_email(self):
        return self.email.replace('@', '-a-').replace('.', '-o-')

    @classmethod
    def from_data(cls, data):
        m = re.search(r'(.*) <(.*)>', data)
        name, email = m.group(1).decode(CHARSET), m.group(2).decode(CHARSET)
        if email in ALIASES:
            omail = email
            email = ALIASES[email]
        else:
            omail = None

        if not email in cls.dictionary:
            obj = cls(email, name)
            cls.dictionary[email] = obj
        else:
            obj = cls.dictionary[email]
        if not name in obj.names:
            obj.names.append(name)
        if omail and omail not in obj.emails:
            obj.emails.append(omail)
        return obj

    @classmethod
    def ranks(cls):
        authors = cls.dictionary.values()
        authors.sort(key=lambda author: -len(author.commits))
        for rank, author in ranking.Ranking(authors, strategy=ranking.FRACTIONAL, start=1, key=lambda author: len(author.commits)):
            yield rank, author


class Group(Author):
    def __init__(self, name='', description=''):
        self.groupname = name
        self.authors = []
        self._description = description

    @property
    def email(self):
        return '<group has no email>'
    
    @property
    def emails(self):
        return [author.email for author in self.authors]

    @property
    def name(self):
        return '<group has no name>'

    @property
    def names(self):
        return [author.name for author in self.authors]

    @property
    def commits(self):
        l = []
        for author in self.authors:
            l += author.commits
        return l

    @property
    def description(self):
        if self._description:
            return self._description
        try:
            return self.settings['description']
        except:
            return ''
    
    @property
    def url(self):
        try:
            return self.settings['url']
        except:
            return None


class Date(object):
    MONTH = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

    def __init__(self, date, timezone, raw=''):
        self.date = date
        self.timezone = timezone
        self.raw = raw

    @property
    def short(self):
        return u'{0}-{1:02}-{2:02} {zone}'.format(self.date.year, self.date.month, self.date.day, zone=self.timezone)

    @classmethod
    def from_data(cls, data):
        m = re.search(r'([A-Z][a-z][a-z]) ([A-Z][a-z][a-z]) ([0-9][0-9]?) (..):(..):(..) (....) ([\+\-]....)', data)
        raw, month, zone = m.group(0), cls.MONTH[m.group(2)], m.group(8)
        day, hour, min, sec, year = [int(m.group(i)) for i in (3, 4, 5, 6, 7)]
        date = datetime.datetime(year, month, day, hour, min, sec)
        obj = cls(date, zone)
        obj.raw = raw
        return obj
        

class Commit(object):
    dictionary = {}
    short_dictionary = {}

    def __init__(self, id, author, date, title, content, merge=[]):
        self.id = id
        self.author = author
        self.date = date
        self.title = title
        self.content = content
        self.merge_ids = merge

    def __repr__(self):
        return u"<Commit('{0}', '{1}', '{2}'>".format(self.id, self.author, self.title, self.abstract)

    @property
    def abstract(self):
        if not self.content:
            return self.title
        if len(self.content) > 40:
            content = self.content[:37] + '...'
        else:
            content = self.content
        return ''.join((self.title, '(', content, ')'))

    @property
    def mergeset(self):
        return [Commit.short_dictionary[merge_id] for merge_id in self.merge_ids]

    @property
    def url(self):
        return COMMIT_URL.format(commit=self.id)

    @classmethod
    def from_data(cls, data):
        merge_ids = []
        try:
            id, zdata = data.split('\nMerge: ', 1)
            mdata, xdata = zdata.split('\nAuthor: ', 1)
            for m in re.finditer(r'[0-9a-f]+', mdata):
                merge_ids.append(m.group(0))
        except:
            id, xdata = data.split('\nAuthor: ', 1)
        adata, ydata = xdata.split('\nDate: ', 1)
        ddata, cdata = ydata.split('\n\n    ', 1)
        title, content = (cdata.split('\n    \n    ', 1) + [None])[:2]
        author = Author.from_data(adata)
        date = Date.from_data(ddata)
        if content:
            content = content[:-1].replace('\n    ', '\n').decode(CHARSET)
        else:
            title = title[:-1]
        obj = cls(id, author, date, title.decode(CHARSET), content, merge_ids)
        cls.dictionary[id] = obj
        cls.short_dictionary[id[:7]] = obj
        author.commits.append(obj)
        return obj


total = Author('total')
active_commits = []
for cdata in data.split('\ncommit '):
    if not cdata: continue
    commit = Commit.from_data(cdata)
    total.commits.append(commit)

timebase = total.commits[0].date.date - datetime.timedelta(days=ACTIVE_DAYS)

authors = []
real_size = 0
others = Group('other')
actives = Group('Active users', 'Users who contributed in the last {0} days'.format(ACTIVE_DAYS))
newfaces = Group('Newfaces', 'Users who contributed his/her first commit in the last {0} days'.format(ACTIVE_DAYS))

active_commits = Author('active')

groups = {}
for gdata in GROUPS:
    group = Group(gdata['name'])
    group.settings = gdata
    groups[group.groupname] = group

for i, (rank, author) in enumerate(Author.ranks()):
    author.tag = author.safe_email
    author.rank = round(rank, 1)
    authors.append(author)
    if i > CHART_SIZE - (len(groups) + 2):
        if not real_size:
            real_size = i
        others.authors.append(author)
    if author.commits[0].date.date >= timebase:
        actives.authors.append(author)
        for commit in author.commits:
            if commit.date.date < timebase:
                break
            active_commits.commits.append(commit)
    if author.commits[-1].date.date >= timebase:
        newfaces.authors.append(author)
    for group in groups.values():
        if group.settings['filter'](author):
            group.authors.append(author)
if not real_size:
    real_size = i

sorted_groups = groups.values()
sorted_groups.sort(key=lambda group: -group.settings.get('priority', 0) * 0x1000000 - len(group.commits))

rendered = template.render(
    TITLE=TITLE, REPO_URL=REPO_URL,
    ACTIVE_DAYS=ACTIVE_DAYS,
    size=real_size, authors=authors, others=others, total=total,
    actives=actives, active_commits=active_commits, newfaces=newfaces,
    groups=sorted_groups,
    numformat=lambda n: '{:,}'.format(n),
)

if OUTPUT_FILE:
    outfile = lopen(OUTPUT_FILE, 'w')
else:
    outfile = sys.stdout
outfile.write(rendered.encode(CHARSET))

if AUTHOR_FILE:
    authors = list(Author.dictionary.values())
    authors.sort(key=lambda author: author.name)
    authorfile = lopen(AUTHOR_FILE, 'w')
    for author in authors:
        authorfile.write(u'{name} <{email}>\n'.format(name=author.name, email=author.email).encode(CHARSET))

