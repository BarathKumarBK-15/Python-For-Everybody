import xml.etree.ElementTree as ET
import sqlite3
conn=sqlite3.connect('SampleDatabase2.sqlite')
c=conn.cursor()
c.executescript('''
drop table if exists Artist;
drop table if exists Album;
drop table if exists Track;
drop table if exists Genre;
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
    len INTEGER, rating INTEGER, count INTEGER
);
''')
fname=input('Enter file name: ')
if len(fname)<1:
    fname='Library.xml'
def lookup(d,key):
    found=False
    for child in d:
        if found:
            return child.text
        if child.tag=='key' and child.text==key:
            found=True
    return None
stuff=ET.parse(fname)
s=stuff.findall('dict/dict/dict')
print('Dict count:',len(s))
for entry in s:
    if lookup(entry,'Track ID') is None:
        continue
    name=lookup(entry,'Name')
    artist=lookup(entry,'Artist')
    album=lookup(entry,'Album')
    genre=lookup(entry,'Genre')
    count=lookup(entry,'Play Count')
    rate=lookup(entry,'Rating')
    length=lookup(entry,'Total Time')
    if name is None or album is None or artist is None or genre is None:
        continue
    c.execute('insert or ignore into Artist(name) values(?)',(artist,))
    c.execute('select id from Artist where name=?',(artist,))
    artist_id=c.fetchone()[0]
    c.execute('insert or ignore into Album(artist_id,title) values(?,?)',(artist_id,album))
    c.execute('select id from Album where title=?',(album,))
    album_id=c.fetchone()[0]
    c.execute('insert or ignore into Genre(name) values(?)',(genre,))
    c.execute('select id from Genre where name=?',(genre,))
    genre_id=c.fetchone()[0]
    c.execute('insert or replace into Track(title,album_id,genre_id,len,rating,count) values(?,?,?,?,?,?)',(name,album_id,genre_id,length,rate,count))
    print(name,album,artist,genre)
conn.commit()
c.close()
