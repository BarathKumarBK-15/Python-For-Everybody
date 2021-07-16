from urllib.request import urlopen
import xml.etree.ElementTree as et
url=input()
uh=urlopen(url)
data=uh.read()
tree=et.fromstring(data)
counts=tree.findall('.//comment')
sum=0
for item in counts:
    sum+=int(item.find('count').text)
print(sum)
