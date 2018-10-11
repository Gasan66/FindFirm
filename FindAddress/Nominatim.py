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
# s = 'екатеринбург, куйбышева 67'
# url = 'https://nominatim.openstreetmap.org/search?format=json&q={0}'.format(urllib.parse.quote(s))
# req = requests.get(url)
# res = req.json()
# response = urllib2.urlopen(url)
# pprint.pprint(res)
# print(url)
# print(urllib.parse.quote(s.decode('utf8').encode('cp1251')))

# cnx_read = mysql.connector.connect(user='admin', password='Qwaszx!2',
#                                      host='100.124.7.179',
#                                      database='FindAddress')

cnx_read = mysql.connector.connect(user='root', password='Gfhjkm1987!',
                                     host='localhost',
                                     database='FinfAddress'
                                     )


cursor_read = cnx_read.cursor(dictionary=True)

# cnx_write = mysql.connector.connect(user='admin', password='Qwaszx!2',
#                                       host='100.124.7.179',
#                                       database='FindAddress')

cnx_write = mysql.connector.connect(user='root', password='Gfhjkm1987!',
                                      host='localhost',
                                      database='FinfAddress'
                                      )


cursor_write = cnx_write.cursor()


def main():
    query = 'SELECT id_address, value FROM FinfAddress.address WHERE isDone <> 1 LIMIT 10'
    cursor_read.execute(query)
    for row in cursor_read:
        address = row.get('value')
        id_address = row.get('id_address')
        write_to_base(id_address, address)


def write_to_base(id_address, address):
    query_osm = ("INSERT INTO osm_address "
                 "(value, id_address) "
                 "VALUES (%(value)s, %(id_address)s)"
                 )
    query_done = 'UPDATE address SET isDone = 1 WHERE id_address = {0}'.format(id_address)
    param = get_param(id_address, address)
    cursor_write.execute(query_osm, param)
    cursor_write.execute(query_done)
    cursor_write.commit()


def get_param(id_adress, address):
    value = get_osm_address(address)
    return {'value': value, 'id_address': id_adress}


def get_osm_address(address):

    url_osm = 'https://nominatim.openstreetmap.org/search?format=json&q={0}'.format(urllib.parse.quote(address))
    response = requests.get(url_osm)
    if response.status_code == 200:
        return response.text
    else:
        return 'Error' + response.status_code


main()
