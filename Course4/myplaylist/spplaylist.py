import json
import sqlite3

conn = sqlite3.connect('playlist.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Connect;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    release_date TEXT,
    total_tracks INTEGER
);

CREATE TABLE Track(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    pop INTEGER,
    len INTEGER,
    album_id INTEGER
);

CREATE TABLE Connect (
    track_id INTEGER,
    artist_id INTEGER,
    PRIMARY KEY (track_id, artist_id)
)
''')

fname = input('Enter FileName: ')
if len(fname) < 1: fname = 'playlist.json'

str_data = open(fname).read()
try:
    js = json.loads(str_data)
except Exception as e:
    print('Unable to Parse JSON:', e)

for item in js['items']:
    album_title = item['track']['album']['name']
    album_release_date = item['track']['album']['release_date']
    total_tracks = item['track']['album']['total_tracks']
    track_title = item['track']['name']
    track_popularity = item['track']['popularity']
    track_duration = item['track']['duration_ms']
    artists = item['track']['artists']

    print((track_title, album_title))

    cur.execute('''INSERT OR IGNORE INTO Album(title, release_date, total_tracks)
                    VALUES (?, ?, ?)''',(album_title, album_release_date, total_tracks) )
    cur.execute('SELECT id FROM Album WHERE title = ?',(album_title, ) )
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Track(title, pop, len, album_id)
                    VALUES (?, ?, ?, ?)''', (track_title, track_popularity, track_duration, album_id ) )
    cur.execute('SELECT id FROM Track WHERE title = ?',(track_title, ) )
    track_id = cur.fetchone()[0]

    for artist in artists:
        name = artist['name']
        cur.execute('INSERT OR IGNORE INTO Artist(name) VALUES (?)', (name, ))
        cur.execute('SELECT id FROM Artist WHERE name = ?', (name,))
        artist_id = cur.fetchone()[0]
        cur.execute('''INSERT OR REPLACE INTO Connect(track_id, artist_id) 
                        VALUES (?, ?)''', (track_id, artist_id))
                        
    conn.commit()

cur.close()
