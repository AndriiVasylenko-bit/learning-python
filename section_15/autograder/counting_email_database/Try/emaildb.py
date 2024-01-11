import sqlite3, re

debag = True

dic = dict()
fname = ''
if not debag:
    fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    org = pieces[1]

    domian = re.search(r'@(.+)$', org).group(1)
    dic[domian] = dic.get(domian, 0) + 1
lst = sorted([(v, k) for (k, v) in dic.items()])
for (k, v) in lst: print(k, v)

conn = sqlite3.connect('email_count2.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''
CREATE TABLE Counts(org TEXT, album_count INTEGER)''')

row = cur.fetchone()
for (v, k) in lst:
    cur.execute('INSERT INTO Counts (org, album_count) VALUES (?, ?)',
                (k, v,))
    conn.commit()
cur.close()