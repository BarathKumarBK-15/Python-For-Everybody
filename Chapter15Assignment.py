import sqlite3
import re
conn=sqlite3.connect('SampleDatabase.sqlite')
c=conn.cursor()
c.execute('drop table if exists Counts')
c.execute('create table Counts(org TEXT,count INTEGER)')
fname=input('Enter file name: ')
if(len(fname)<1):
    fname='mbox.txt'
f=open(fname)
for line in f:
    if line.startswith('From: '):
        words=line.split()
        d=re.findall('@(\S+)',words[1])
        c.execute('select count from Counts where org=?',(d[0],))
        row=c.fetchone()
        if row is None:
            c.execute('insert into Counts(org,count) values(?,1)',(d[0],))
        else:
            c.execute('update Counts set count=count+1 where org=?',(d[0],))
conn.commit()
dis='select * from Counts order by count desc limit 10'
for row in c.execute(dis):
    print(str(row[0]),row[1])
c.close()
