import sqlite3

# створення з'єднання з базою даних SQLite
conn = sqlite3.connect('emaildb.sqlite')
# створення об'єкта курсора
cur = conn.cursor()

# використовується для виконання SQL запитів у базі даних
cur.execute('''drop table if exists counts''')
cur.execute('''create table counts (email text, count integer)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    # вибрати count із counts де email = email
    cur.execute('select count from counts where email = ? ', (email,))
    # вертає результат вибірка (радка).
    row = cur.fetchone()
    if row is None:
        # вставити у counts (email, count) значення (email, 1)
        cur.execute('insert into counts (email, count) values (?, 1)', (email,))
    else:
        # обновити counts задати count = count + 1 де email = email
        cur.execute('update counts set count = count + 1 where email = ?', (email,))
    conn.commit()  # фиксация

# https://www.sqlite.org/lang_select.html
# вибрати email, count з counts у порядку зменшення count тільки 10 рядків
sqlstr = 'select email, count from counts order by count desc limit 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
