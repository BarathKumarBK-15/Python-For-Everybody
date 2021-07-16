from urllib.request import urlopen
import json
url=input('Enter location:')
print('Retrieving', url)
uh=urlopen(url)
data=uh.read().decode()
js=json.loads(data)
print('Retrieved',len(data),'characters')
count=0
sum=0
l=js['comments']
for i in l:
    count+=1
    sum+=int(i['count'])
print('Count:',count)
print('Sum:',sum)
