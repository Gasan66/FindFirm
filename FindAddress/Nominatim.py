# from nominatim import Nominatim
import sys
# if sys.version_info.major == 2:
#     import urllib2
# else:
import requests
import pprint
import urllib.request as urllib2
import urllib.parse
import mysql.connector

# nom = Nominatim()

# address = '58 Parker Street London'

# t = nom.query(address)
s = 'екатеринбург, куйбышева 67'
url = 'https://nominatim.openstreetmap.org/search?format=json&q={0}'.format(urllib.parse.quote(s))
req = requests.get(url)
res = req.json()
# response = urllib2.urlopen(url)
pprint.pprint(res)
# print(url)
# print(urllib.parse.quote(s.decode('utf8').encode('cp1251')))

cnx_read = mysql.connector.connect(user='admin', password='Qwaszx!2',
                                     host='100.124.7.179',
                                     database='FindAddress')

cursor_read = cnx_read.cursor(dictionary=True)

cnx_write = mysql.connector.connect(user='admin', password='Qwaszx!2',
                                      host='100.124.7.179',
                                      database='FindAddress')
cursor_write = cnx_write.cursor()


def main():
    query = 'SELECT id, value FROM FindAddress.address WHERE isDone <> 1'
    cursor_read.execute(query)
    for row in cursor_read:
        address = row.get('value')
        id = row.get('id')
        write_to_base(id, address)


def write_to_base(id, address):
    query = ("INSERT INTO yandex_address "
             "(id, value, id_address) "
             "VALUES (%(id_osm)s, %(value)s, %(id_address)s)")
    param = get_param(id, address)
    cursor_write.execute(query, param)
    cursor_write.commit()


def get_param(id, address):
    id_osm = ''  # попробовать проверить фишку с ключом, чтобы добавлялся сам при добавлении записи в базе.
    value = get_osm_address(address)
    return {'id_osm': id_osm, 'value': value, 'id_address': id}


def get_osm_address(address):

    url_osm = 'https://nominatim.openstreetmap.org/search?format=json&q={0}'.format(urllib.parse.quote(address))
    response = requests.get(url_osm)
    if response.status_code == 200:
        return response.text
    else:
        return 'Error' + response.status_code
