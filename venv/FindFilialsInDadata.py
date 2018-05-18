import mysql.connector
test = []
cnx_in = mysql.connector.connect(user='root', password='Gfhjkm1987',
                                 host='127.0.0.1',
                                 database='FindFirm')
cnx_out = mysql.connector.connect(user='root', password='Gfhjkm1987',
                                 host='127.0.0.1',
                                 database='FindFirm')
cursor_in = cnx_in.cursor(dictionary=True)
cursor_out = cnx_out.cursor()

query = 'SELECT INN, City FROM Input_data LIMIT 100'
query_1 = ("INSERT INTO output_filial "
           "(NameDadata , NameDadataShort , INN , Branch_type , Branch_count , OPF , Name_full_with_opf , "
           "Name_short_with_opf , Address_value , Address_unrestricted_value , Geo_lat , Geo_lon, City) "
           "VALUES (457, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)")

cursor_in.execute(query)

cursor_out.execute(query_1)
cnx_out.commit()

for row in cursor_in:
    print(row)

cursor_in.close()
cursor_out.close()
cnx_in.close()
cnx_out.close()
