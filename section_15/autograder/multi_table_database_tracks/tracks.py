import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript(''' 
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, album_rating INTEGER, album_count INTEGER
);
''')

# fname = input('Enter file name: ')
# if (len(fname) < 1):
fname = 'Library.xml'


# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None


stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict album_count:', len(all))
for entry in all:
    if (lookup(entry, 'Track ID') is None): continue

    track_name = lookup(entry, 'Name')
    artist_text = lookup(entry, 'Artist')
    genre_name = lookup(entry, 'Genre')
    album_title = lookup(entry, 'Album')
    album_count = lookup(entry, 'Play Count')
    album_rating = lookup(entry, 'Rating')
    album_length = lookup(entry, 'Total Time')

    if track_name is None or artist_text is None or album_title is None:
        continue

    print(track_name, artist_text, genre_name, album_title, album_count, album_rating, album_length)

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', (genre_name,))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre_name,))
    genre_row = cur.fetchone()
    if genre_row is None: continue
    genre_id = genre_row[0]

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', (artist_text,))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist_text,))
    artist_row = cur.fetchone()
    if artist_row is None: continue
    artist_id = artist_row[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', (album_title, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album_title,))
    album_row = cur.fetchone()
    if album_row is None: continue
    album_id = album_row[0]

    cur.execute('''INSERT OR IGNORE INTO Track
        (title, album_id, genre_id, len, album_rating, album_count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''',
                (track_name, album_id, genre_id, album_length, album_rating, album_count))

cur.execute('''
SELECT Track.title, Artist.name, Album.title, Genre.name
FROM Track JOIN Genre JOIN Album JOIN Artist
ON Track.genre_id = Genre.ID and Track.album_id = Album.id
AND Album.artist_id = Artist.id
ORDER BY Artist.name LIMIT 3
''')
tracks = cur.fetchall()
for track in tracks: print(track)
conn.commit()
cur.close()
