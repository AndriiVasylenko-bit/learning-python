import sqlite3, re

debag = True


conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = ''
if not debag: fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    org = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count'

dic = dict()
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
    domian = re.search(r'@(.+)$', row[0]).group(1)
    dic[domian] = dic.get(domian, 0) + row[1]

lst = sorted([(v, k) for (k, v) in dic.items()])
for (k, v) in lst: print(k, v)

# print('Sum org: ', sum(count))
# print('Max org: ', max(count))


cur.close()