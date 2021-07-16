from urllib.request import urlopen
from urllib.parse import urlencode
import json
serviceurl='https://maps.googleapis.com/maps/api/geocode/json?'
add=input('Enter location:')
url=serviceurl+urlencode({'address':add,'key':'AIzaSyBByVJxJIb7qZHibBQX5D3LuH4_lKH8J7s'})
print('Retrieving',url)
uh=urlopen(url)
data=uh.read().decode()
js=json.loads(data)
print(data)
print(js['results'][0]['geometry']['location'])
print(js['results'][0]['formatted_address'])
