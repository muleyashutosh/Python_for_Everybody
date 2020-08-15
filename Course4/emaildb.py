import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')
curr = conn.cursor()


curr.execute('DROP TABLE IF EXISTS Counts')

curr.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter File Name: ')
if len(fname) < 1: fname = 'mbox-short.txt'
fname = open(fname)
for line in fname:
    if not line.startswith('From: ') : continue
    email = line.split()[1]
    org = re.findall('@(.*)', email)[0]
    curr.execute('SELECT count FROM Counts WHERE org = ?',(org,))
    row = curr.fetchone()
    if row is None:
        curr.execute('INSERT INTO Counts(org,count) VALUES (? ,1)', (org,))
    else:
        curr.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,) )
    
conn.commit()
sqlstring = 'SELECT org,count FROM Counts ORDER BY count DESC LIMIT 10'

for org,count in curr.execute(sqlstring):
    print(org,count)

curr.close()




