# -*- coding: utf-8 -*-
# See settings.py for more options

TITLE = 'Servo commit statistics'

TEMPLATE_FILE = 'template.html'
INPUT_FILE = 'log.txt' # None for stdin
OUTPUT_FILE = None # None for stdout
AUTHOR_FILE = 'authors.txt'

COMMIT_DETAIL_COUNT = 1
COMMIT_ABSTRACT_COUNT = 5
COMMIT_LIST_COUNT = 20

REPO_URL = 'https://github.com/mozilla/servo/tree/master'
COMMIT_URL = 'http://github.com/mozilla/servo/commit/{commit}'
ACTIVE_DAYS = 30

GITHUB_RIBBON = 'https://github.com/youknowone/gitstat/tree/servostat'

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
    'metajack+bors@gmail.com': 'release+servo@mozilla.com',
    'Manishearth@users.noreply.github.com': 'manishsmail@gmail.com',
    'cavalcantii@gmail.com': 'a.cavalcanti@samsung.com',
    'a.cavalcanti@sisa.samsung.com': 'a.cavalcanti@samsung.com',
    'andersrb@gmail.com': 'banderson@mozilla.com',
    'brunoabinader@gmail.com': 'bruno.d@partner.samsung.com',
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
    'me@luqman.ca': 'laden@csclub.uwaterloo.ca', # reverse?
    'laden@mozilla.com': 'laden@csclub.uwaterloo.ca', # reverse?
    'eholk@mozilla.com': 'eric.holk@gmail.com', # reverse?
    'eslaughter@mozilla.com': 'elliottslaughter@gmail.com', #reverse? 
    'lkuper@mozilla.com': 'lindsey@composition.al', #reverse?
}

MOZILLA = ["josh@joshmatthews.net", "jack@metajack.im", "gw@intuitionlibrary.com", "mbrubeck@limpet.net", "niko@alum.mit.edu", "bobbyholley@gmail.com", "james@hoppipolla.co.uk", "joshmoz@gmail.com",
           "sean.monstar@gmail.com", "andersrb@gmail.com", "shout@ozten.com", "bzbarsky@mit.edu", "ben@wanderview.com", "simon.sapin@exyr.org", "fabrice@desre.org"]
SAMSUNG = ["sanxiyn@gmail.com", "hykim0777@gmail.com", "michael.blumenkrantz@gmail.com", "jun0cho@gmail.com", "cavalcantii@gmail.com", "brunoabinader@gmail.com"]
COMMUNITY = ["ms2ger@gmail.com", "saneyuki.snyk@gmail.com", "saurabhanandiit@gmail.com", "utatane.tea@gmail.com", "sankha93@gmail.com", "daniel@glazman.org", "evilpies@gmail.com",
             "pylaurent1314@gmail.com", "manishsmail@gmail.com"]

GROUPS = [
    {
        'name': 'Bot',
        'description': 'Robot is your friend', # -- sanxiyn
        'filter': lambda author: author.name == 'bors',
        'priority': 1,
    },
    {
        'name': 'Mozilla Corporation',
        'url': 'http://www.mozilla.org/',
        'filter': lambda author: author.email in MOZILLA or '@mozilla.com' in author.email,
    },
    {
        'name': 'Samsung Electronics',
        'url': 'http://www.samsung.com/',
        'filter': lambda author: '@samsung.com' in author.email or author.email in SAMSUNG,
    },
    {
        'name': 'Igalia',
        'filter': lambda author: '@igalia.com' in author.email,
    },
    {
        'name': 'Mozilla Community',
        'filter': lambda author: author.email in COMMUNITY,
    },
    {
        'name': 'Unidentified',
        'description': 'Strange emails...',
        'filter': lambda author: author.email.endswith('(none)') or author.email.endswith('.localdomain')
    },
]
