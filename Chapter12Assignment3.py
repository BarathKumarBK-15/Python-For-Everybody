from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re
url=input('Enter URL: ')
count=int(input('Enter count:'))
pos=int(input('Enter position:'))
html=urlopen(url).read()
s=bs(html,'html.parser')
t=s('a')
while count>0:
    url=t[pos-1].get('href',None)
    html=urlopen(url).read()
    s=bs(html,'html.parser')
    t=s('a')
    count-=1
answer=re.findall('by_(\S+?)\.',url)
print(answer[0])
