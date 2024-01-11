import sqlite3, re

debag = True


conn = sqlite3.connect('email_count2.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, album_count INTEGER)''')

fname = ''
if not debag: fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    org = pieces[1]
    cur.execute('SELECT album_count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, album_count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET album_count = album_count + 1 WHERE org = ?',
                    (org,))
conn.commit()

# https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT org, album_count FROM Counts ORDER BY album_count'
#
# dic = dict()
# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])
#     domian = re.search(r'@(.+)$', row[0]).group(1)
#     dic[domian] = dic.get(domian, 0) + row[1]
#
# lst = sorted([(v, k) for (k, v) in dic.items()])
# for (k, v) in lst: print(k, v)

# print('Sum org: ', sum(album_count))
# print('Max org: ', max(album_count))


cur.close()