from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
url=input("Enter -")
html=urlopen(url).read()
s=bs(html,"html.parser")
tags=s('span')
sum=0
for tag in tags:
    sum+=int(tag.contents[0])
print(sum)
