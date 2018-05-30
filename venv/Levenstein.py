'''
Скрипт для нечеткого вравнения названий фирм
'''



import Levenshtein as lev
import dgis
import requests
import json
import time
import mysql.connector


start_time = time.time()
cnx_in = mysql.connector.connect(user='root', password='Gfhjkm1987',
                                 host='127.0.0.1',
                                 database='FindFirm')

cnx_out = mysql.connector.connect(user='root', password='Gfhjkm1987',
                                 host='127.0.0.1',
                                 database='FindFirm')

cursor_in = cnx_in.cursor(dictionary=True)
cursor_out = cnx_out.cursor()


query = 'select NameDadata, NameDadataShort, NameYandex, id from output_main_copy'

query_done = 'UPDATE output_main_copy SET Lev_dadata_yandex = %(Lev_Dadata_Yandex)s, ' \
             'Lev_DadataShort_Yandex = %(Lev_DadataShort_Yandex)s where id = %(id)s'

cursor_in.execute(query)

lev_dict = {}
i = 0
for row in cursor_in:
    lev_dict['NameDadata'] = row.get('NameDadata')
    lev_dict['NameDadataShort'] = row.get('NameDadataShort')
    lev_dict['NameYandex'] = row.get('NameYandex')
    lev_dict['id'] = row.get('id')
    lev_dict['Lev_Dadata_Yandex'] = lev.ratio(str(row.get('NameYandex')).lower(), str(row.get('NameDadata')).lower())
    lev_dict['Lev_DadataShort_Yandex'] = lev.ratio(str(row.get('NameDadataShort')).lower(), str(row.get('NameYandex')).lower())

    cursor_out.execute(query_done, lev_dict)
    cnx_out.commit()
    i += 1
    print(i)

print("--- %s seconds ---" % (time.time() - start_time))
