import json
import sqlite3
conn=sqlite3.connect('SampleDatabase3.sqlite')
c=conn.cursor()
c.executescript('''
drop table if exists User;
drop table if exists Course;
drop table if exists Member;
create table User(
    id integer not null primary key autoincrement unique,
    name text unique
);
create table Course(
    id integer not null primary key autoincrement unique,
    title text unique
);
create table Member(
    user_id integer,
    course_id integer,
    role integer,
    primary key(user_id,course_id)
)
''')
fname=input('Enter file name: ')
if len(fname)<1:
    fname='roster_data.json'
data=open(fname).read()
j=json.loads(data)
for i in j:
    name=i[0]
    title=i[1]
    role=i[2]
    print(name,title,role)
    c.execute('insert or ignore into User(name) values(?)',(name,))
    c.execute('select id from User where name=?',(name,))
    user_id=c.fetchone()[0]
    c.execute('insert or ignore into Course(title) values(?)',(title,))
    c.execute('select id from Course where title=?',(title,))
    course_id=c.fetchone()[0]
    c.execute('insert or replace into Member(user_id,course_id,role) values(?,?,?)',(user_id,course_id,role))
conn.commit()
c.close()
