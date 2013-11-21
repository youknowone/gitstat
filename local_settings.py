
#-*- coding: utf-8 -*-
TITLE = 'Rust Language'

TEMPLATE_FILE = 'template.html'
INPUT_FILE = 'log.txt' # None for stdin
OUTPUT_FILE = None # None for stdout
AUTHOR_FILE = 'authors.txt'

COMMIT_DETAIL_COUNT = 1
COMMIT_ABSTRACT_COUNT = 5
COMMIT_LIST_COUNT = 20

REPO_URL = 'https://github.com/mozilla/rust/tree/master'
COMMIT_URL = 'http://github.com/mozilla/rust/commit/{commit}'
ACTIVE_DAYS = 30

GITHUB_RIBBON = 'https://github.com/youknowone/gitstat/tree/ruststat'

GOOGLE_ANALYTICS = 'UA-28402752-3', 'youknowone.org'

NAMES = {
    'elly@leptoquark.net': 'Elly Fong-Jones',
    'garethdanielsmith@gmail.com': 'Gareth Daniel Smith',
    'ben@jackman.biz': 'Benjamin Jackman',
    'cpressey@gmail.com': 'Chris Pressey',
    'eric@ejholmes.net': 'Eric Holmes',
    'graydon@mozilla.com': 'Graydon Hoare',
    'sbarberdueck@gmail.com': 'Simon Barber-Dueck',
    'robarnold@cs.cmu.edu': 'Rob Arnold',
    'ilyoan@gmail.com': 'Ilyong Cho',
    'respindola@mozilla.com': u'Rafael Ávila de Espíndola',
    'tohava@gmail.com': 'Or Brostovski',
    'kyeongwoon.lee@samsung.com': 'Kyeongwoon Lee',
    'tdixon51793@gmail.com': 'startling',
    'alex@lycus.org': u'Alex Rønne Petersen',
    'damien.schoof@gmail.com': 'Damien Schoof',
    'github@kudling.de': 'Lennart Kudling',
}

ALIASES = {
    'graydon@pobox.com': 'graydon@mozilla.com', # Make a@ as alias of b@
    'graydon@4632428-PC.(none)': 'graydon@mozilla.com',
    'as@hacks.yi.org': 'mad.one@gmail.com',
    'andersrb@gmail.com': 'banderson@mozilla.com',
    'etryzelaar@iqt.org': 'erick.tryzelaar@gmail.com',
    'jason.orendorff@gmail.com': 'jorendorff@mozilla.com',
    'jason@mozmac-2.local': 'jorendorff@mozilla.com',
    'clements@brinckerhoff.org': 'clements@racket-lang.org',
    'jyyou.tw@gmail.com': 'jyyou@cs.nctu.edu.tw',
    'lindsey@rockstargirl.org': 'lkuper@mozilla.com',
    'lindsey@composition.al': 'lkuper@mozilla.com',
    'espindola@dream.(none)': 'respindola@mozilla.com',
    'robarnold@68-26-94-7.pools.spcsdns.net': 'robarnold@cs.cmu.edu',
    'catamorphism@gmail.com': 'chevalier@alum.wellesley.edu',
    'tohava@tohava-laptop.(none)': 'tohava@gmail.com',
    'zackcorr95@gmail.com': 'zack@z0w0.me',
    'gareth@gareth-N56VM.(none)': 'garethdanielsmith@gmail.com',
    'makoto.nksm@gmail.com': 'makoto.nksm+github@gmail.com',
    'andreas.gal@gmail.com': 'gal@mozilla.com',
    'spicyjalapeno@gmail.com': 'ben@benalpert.com',
    'simon.sapin@exyr.org': 'simon@exyr.org',
    'pcwalton@mimiga.net': 'pwalton@mozilla.com',
    'simon@server': 'sbarberdueck@gmail.com',
    'public+git@mearie.org': 'kang.seonghoon@mearie.org',
    'mbrubeck@cs.hmc.edu': 'mbrubeck@limpet.net',
    'mmeyerho@andrew': 'mmeyerho@andrew.cmu.edu',
    'ysson83@gmail.com': 'ysoo.son@samsung.com',
    '=125axel125@gmail.com': 'mark.edward.x@gmail.com',
    'B.Steinbrink@gmx.de': 'bsteinbr@gmail.com',
    'georges.dubus@gmail.com': 'georges.dubus@compiletoi.net',
    'Heather@cynede.net': 'heather@cynede.net',
    'yjh0502@gmail.com': 'jihyun@nclab.kaist.ac.kr',
    'sstewartgallus00@mylangara.bc.ca': 'sstewartgallus00@langara.bc.ca',
    'me@luqman.ca': 'laden@csclub.uwaterloo.ca', # reverse?
    'laden@mozilla.com': 'laden@csclub.uwaterloo.ca', # reverse?
    'eholk@mozilla.com': 'eholk@cs.indiana.edu',
    'eric.holk@gmail.com': 'eholk@cs.indiana.edu',
    'eslaughter@mozilla.com': 'elliottslaughter@gmail.com', #reverse? 
    'ereed@mozilla.com': 'ecreed@cs.washington.edu',
    'bruphili@student.ethz.ch': 'blei42@gmail.com',
}

GROUPS = [
    {
        'name': 'Bot',
        'description': 'Robot is your friend', # -- sanxiyn
        'filter': lambda author: author.name == 'bors',
        'priority': 1,
    },
    {
        'name': 'Mozilla',
        'url': 'http://www.mozilla.org/',
        'filter': lambda author: author.email.endswith('@mozilla.com') or author.email in ['pcwalton@mimiga.net', 'chevalier@alum.wellesley.edu', 'niko@alum.mit.edu', 'sully@msully.net', 'eric.holk@gmail.com', 'elliottslaughter@gmail.com', 'laden@csclub.uwaterloo.ca' ],
    },
    {
        'name': 'Samsung Electronics',
        'url': 'http://www.samsung.com/',
        'filter': lambda author: '@samsung.com' in author.email or author.email in ['sanxiyn@gmail.com', 'ilyoan@gmail.com', 'ladinjin@hanmail.net', 'vivekgalatage@gmail.com'],
    },
    {
        'name': 'Korean Rust User Group',
        'url': 'http://rust-kr.org/', # written in Rust!
        'filter': lambda author: author.email in ['sanxiyn@gmail.com', 'kang.seonghoon@mearie.org', 'jeong@youknowone.org', 'jihyun@nclab.kaist.ac.kr', 'klutzytheklutzy@gmail.com', 'wdlee91@gmail.com'],
    },
    {
        'name': 'Unidentified',
        'description': 'Strange emails...',
        'filter': lambda author: author.email.endswith('(none)') or author.email.endswith('debian.localdomain'),
    },
]
