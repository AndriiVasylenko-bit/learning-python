import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()  # descriptor

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE);
    
CREATE TABLE "Album" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    artist_id INTEGER,
    "title" TEXT UNIQUE);

CREATE TABLE "Track" (
    "id" INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    len INTEGER, album_rating INTEGER, album_count INTEGER);
''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'Library.xml'


# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>

# Root validation.
def lookup(element, key):
    found = False
    for child in element:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None


stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')  # List all element 'dict'.
print('Dict album_count: ', len(all))
for element in all:
    if (lookup(element, 'Track ID') is None): continue  # Root validation.

    name = lookup(element, 'Name')  # Root validation.
    artist = lookup(element, 'Artist')  # Root validation.
    album = lookup(element, 'Album')  # Root validation.
    count = lookup(element, 'Play Count')  # Root validation.
    rating = lookup(element, 'Rating')  # Root validation.
    length = lookup(element, 'Total Time')  # Root validation.

    if name is None or artist is None or album is None:  # Root validation.
        continue

    print(name, artist, album, rating, length)

    # Work only SQLLight
    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
    artist_id = cur.fetchone()[0]

    # Work only SQLLight
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES (?, ?)''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album,))
    album_id = cur.fetchone()[0]

    # Work only SQLLight
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, album_rating, album_count)
        VALUES (?, ?, ?, ?, ?)''',
                (name, album_id, length, rating, count))

    conn.commit()
