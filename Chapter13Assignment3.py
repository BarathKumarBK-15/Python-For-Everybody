from urllib.request import urlopen
from urllib.parse import urlencode
import json
serviceurl='http://py4e-data.dr-chuck.net/json?'
add=input('Enter location:')
url=serviceurl+urlencode({'address':add,'key':42})
print('Retrieving',url)
uh=urlopen(url)
data=uh.read().decode()
js=json.loads(data)
print(js['results'][0]['place_id'])
