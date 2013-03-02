gitstat
=======

Simple, static git statistics generator

Install
-------
````
$ git clone git://github.com/youknowone/gitstat.git
$ cd gitstat
# pip install -r requirements.txt
$ cp settings.py.example settings.py
$ edit settings.py # set title and input/output
````

Test
----
````
$ cd <your-git-repo>
$ git log | <gitstat-dir>/gen.py > log.txt # for stdin/stdout
or
$ git log > log.txt && <gitstat-dir>/gen.py > log.txt # for infile/stdout
or
$ git log > log.txt && <gitstat-dir>/gen.py # for infile/outfile
````

Auto-refresh
------------
Use crontab

`crontab -e` to edit list and add upper test script.
