# from nominatim import Nominatim
import sys
# if sys.version_info.major == 2:
#     import urllib2
# else:
import requests
import pprint
import urllib.request as urllib2
import urllib.parse

# nom = Nominatim()

# address = '58 Parker Street London'

# t = nom.query(address)
# url = 'https://nominatim.openstreetmap.org/search?format=json&q=москва,%20кутузовский%20проспект,%2032'
# req = requests.get(url)
# res = req.json()
# response = urllib2.urlopen(url)
# pprint.pprint(res)
s = 'москва'
print(urllib.parse.quote(s))
# print(urllib.parse.quote(s.decode('utf8').encode('cp1251')))
