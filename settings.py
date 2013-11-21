
#-*- coding: utf-8 -*-
TITLE = 'Page Title'

CHART_SIZE = 70 # Maybe Google limit?
CHARSET = 'utf-8'

TEMPLATE_FILE = 'template.html'
INPUT_FILE = None # None for stdin
OUTPUT_FILE = None # None for stdout
AUTHOR_FILE = 'authors.txt'

COMMIT_DETAIL_COUNT = 1
COMMIT_ABSTRACT_COUNT = 5
COMMIT_LIST_COUNT = 20

REPO_URL = 'https://github.com/youknowone/gitstat/tree/master'
COMMIT_URL = 'http://github.com/youknowone/gitstat/commit/{commit}'
ACTIVE_DAYS = 30

GITHUB_RIBBON = None

GOOGLE_ANALYTICS = 'UA-28402752-3', 'youknowone.org'

NAMES = {
    # 'email@example.com': 'Commit Name',
}

ALIASES = {
    # 'email1@example.com': 'email2@example.com', # Make email1 as alias of email2
}

GROUPS = [
    #{
    #    'name': 'Users', # name of group
    #    'description': 'Description of user group', # description of group
    #    'filter': lambda author: 'YunWon' in author.name, # filter by author
    #    'priority': 1, # optional
    #},
]

from local_settings import *

