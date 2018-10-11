import requests
import json
# import pprint
import time
# import mysql.connector


cnx_in = mysql.connector.connect(user='admin', password='Qwaszx!2',
                                 host='100.124.7.179',
                                 database='FindAddress')

cnx_out = mysql.connector.connect(user='admin', password='Qwaszx!2',
                                  host='100.124.7.179',
                                  database='FindAddress')

cursor_in = cnx_in.cursor(dictionary=True)
cursor_out = cnx_out.cursor()

query = 'SELECT id, value FROM FindAddress.address WHERE isDone <> 1'

query_yandex_address = ("INSERT INTO yandex_address "
                        "(id, value, id_address) "
                        "VALUES (%(id)s, %(value)s, %(id_address)s)")

query_done = 'UPDATE address SET isDone = 1 WHERE id_address = %(id)s'

yandex_key = {'true': '0be20c72-8a9d-4fc0-be55-320d5048a68e'
              , 'other': ['0cbc01a5-fe7e-4ada-b587-37f5180b5af3'
                            , 'aafff3ab-15a3-489a-b129-e1caf80c6c8e'
                            , 'b8f5a7f2-9a0c-4aa6-ab3f-5681ff78ff67'
                            , '786386b9-13e7-4526-ac14-885cbbab24ae'
                            , '11c449dc-8e6b-4a01-84d0-066975266334'
                            , 'f2106ce9-2cc7-4a12-9be4-5f7129fbcd5b'
                            , 'c0bdf248-ac07-4aaf-9774-50799f79d66d'
                            , 'e2d13b8c-e2c8-4564-b7a4-a1a2c7419899'
                            , '33a854fd-c860-4f33-a9cc-9f76665a982c'
                            , 'c12b2181-2786-44c5-a923-542f553ae810'
                            , '54c4b532-b4c8-4c79-bcac-db100d162fbb'
                            , '64c56031-6922-4691-90e6-71d9116e51fb'
                            , '11f51a42-beed-4767-a81d-a3e811c7a273'
                            , '9b92245f-3e19-431e-ab6b-cf4063cbd0ba'
                            , '6f756b9a-3043-41be-866b-817773bdd8ca'
                            , '8379518d-de8e-46d2-97cf-953eaafe1cb4'
                            , 'ce792659-ba94-49b3-b435-9dee7c64c493'
                            , '070e7d12-798d-4f7d-853c-ae395a6b7fd4'
                            , '45fa4ad5-160b-45c9-8293-a3d4d0ba5228'
                            , 'e395e715-a06f-47c9-a82c-8a346c017f1f'
                            , 'e11d0a58-e033-4853-847b-bcbca83dc98d'
                            , '0ad21802-7fbf-4ea7-aa55-43f429819517'
                            , '685c6e11-0a0a-4596-8bee-82708c6359bd'
                            , '54a8e410-f417-4ec8-81ff-22e511eb7842'
                            , '9488fcb2-b77d-451e-b8a8-1a97506449de'
                            , '9024b7e5-d3a7-46d1-bbeb-61ec2a3be4df'
                            , '40515ef0-0415-42d4-ae36-c553ce4adcff'
                            , '80c359a1-391a-4195-8c26-71a8a5c046bd'
                            , 'c6de7b1e-54c9-49ae-9744-d89b0fc9a4df'
                            , '9aba3641-8c1f-4d5d-a626-a4ace12d1538'
                            , '5d48150d-d787-4f9b-872a-5ae1bbe32f46'
                            , '72cc4629-c745-4681-ae6a-b247b4bd6bc7'
                            , '969f5f68-1564-4c8f-9457-31521feae16f'
                            , '0818ab2b-ad3e-4553-a365-6b04fa62db75'
                            , '82ac6eb9-21f6-4bb5-a73c-716533e71ef3'
                            , 'f569454d-d14d-4233-8d75-2b59256a3099'
                            , 'fec72a92-51bb-45f7-84fc-268e88fb88dd'
                            , 'cc5f7cda-83d1-4e8b-862f-ac01884cae82'
                            , 'cfd8b160-f826-4020-8ea7-629d65c068b5'
                            , '55a6fa2a-61aa-49e8-a95a-3335ceeaf6db'
                            , 'c5281863-7aa4-48b9-b219-0388a9c647b7'
                            , '99626ac7-a008-4593-b02b-eade8a7c9f99'
                            , '04ba5f50-245f-44ba-b80c-64e3f95c5f31'
                            , '70926791-5348-4efb-b0c2-a2b7e1e8139a'
                            , '3a48ea9a-56b8-49dd-a7d4-edad286bf897'
                            , 'f36eb719-778d-4e6e-9f71-1eaa969f734c'
                            , '4044daf9-97f0-4426-b1fd-660288ae038d'
                            , '7c54d631-d33c-40a7-acfd-8c256e0899b7'
                            , 'fdf89fe7-f55a-4f8f-8332-23110effef9d'
                            , '3b341b67-ae03-4465-a271-98fb1c75667d'
                            , 'efcc4325-a558-4900-b47d-297ebe680313'
                            , '15a50d98-6c52-4707-ad4c-a18bd8837c4c'
                            , '95c6b422-5ba2-4825-9a57-3d2926228481'
                            , 'd988ca52-db7f-4e1f-89b5-c286b123eb37'
                            , 'ac363f9f-b015-4fd3-bd35-736b71ac8aff'
                            , 'b4953a44-a49a-4127-a193-d1f6259fa850'
                            , '630615ea-6f16-4284-9402-34da0929b18f'
                            , '10587c68-f311-4189-ac94-1a4e93adc2d0'
                            , 'b8d0a0ce-1fd8-4a31-8e8e-9297e64a1c9a'
                            , '2446ef45-b04a-4d2e-8a05-5c8e8fdd9ffc'
                            , 'e83e453e-ee76-408d-a63e-48bfa95adae7'
                            , '0b1cd711-16af-4faf-a76a-08e60d7c9b2b'
                            , '99664621-6514-4bab-b7e7-59c9e9161596'
                            , '3671eff8-9ea3-4967-94da-01e9eabac2d1'
                            , '2498ff6c-567a-47ed-8c55-1ea58fce7008'
                            , '04503e1d-4fb6-498a-984c-979ecfb3b6a9'
                            , '98224d5b-c629-490d-ad2b-8c69cf4ce6fb'
                            , '8d68f0cb-4d0a-4db0-b126-56ab6d8bbd95'
                            , '1cced0d4-63c8-43ca-b759-24299fa436d9'
                            , 'fb348b3a-9681-4a6e-a709-59eb3063853e'
                            , 'b73a3d09-55d5-4171-8b03-98e7cca74427'
                            , '75712d60-f431-4433-97d0-0f0497279df8'
                            , '294d95c5-096c-4855-ac4d-3312a40af599'
                            , '5ecc1582-33b3-4fd3-9569-d88dea234a6d'
                            , '154389c5-bc6c-4561-be53-27d4905c9c95'
                            , '1ec05f9f-3431-468e-b96d-0bf396567f5f'
                            , '0a445ccb-6cea-4648-a28e-6c2c1c945637'
                            , '324bf286-a98c-4edf-b1ab-ba60ad66b4c0'
                            , 'cc08031f-cc53-450c-aae4-009b504ed58c'
                            , '30fe37e0-3ce6-46df-b089-771af5d2fb1d'
                            , '0f990efd-5463-4498-a104-8ccb696c12e6'
                            , 'dc4ff363-25b8-4fbc-a8a2-a9fca3127bf9'
                            , '53e5b051-31e4-4947-8d1e-387195afed33'
                            , '51e6ec70-f613-4224-8202-f1d5c1a9ef32'
                            , '0e0c515b-2747-4b97-913f-b562cb0f8a58'
                            , '796ebfdd-9294-4c34-b9a5-0a85dc964aab'
                            , '0be30470-2c67-4f77-99ea-8139c42ea9db'
                            , 'c99693ec-e5ac-46ac-b3de-6d66b5af9a2d'
                            , '1d499653-4695-400f-82ca-d92f7cc849b5'
                            , 'bf062a14-c142-4161-a97b-977b9f437aaf'
                            , '4ec6e22c-2a7a-49c8-bc04-7fca4bf9ba8b'
                            , '0d65efe8-cff8-497e-84ab-58b3086264da'
                            , '5722d7b3-f1d9-4271-9f6d-56c6969341d2'
                            , 'aacc7c79-aefd-4b47-8341-7d36841240d1'
                            , 'ca5d3952-8394-4d78-8ff8-1a91707bc2b6'
                            , 'ed1210ad-a188-49e0-8849-278af09c17b1'
                            , '43afcdc6-c38c-4caf-a98f-3ec2f732635a'
                            , '52e44eb9-4ddd-48df-96f1-7075c78e7f31'
                            , '38e8b553-06f5-457a-8696-0a6d3de95be0'
                            , 'fcc7d9cb-fc9b-41a3-8017-eb8364bf624c'
                            , 'cdd16f74-6f25-4335-b0d3-a76e2d2ce352'
                            , 'c0c7d364-e5b9-4406-b00f-b5c6655a657b'
                            , '5d4eaf49-b038-472a-8457-d9c3af411ef9'
                            , '67f80340-eae1-496f-9caf-56d471e97ffb'
                            , '04d54ce8-699d-436f-97be-291bdf35f6be'
                            , 'a2707250-f224-4cb4-95dc-d657ca33ebfe'
                            , '812b4f0a-da43-4251-b2f4-253c5f6c8d2d'
                            , 'df4fcf3f-9725-493a-9b7d-c5d3981ea7e4'
                            , '897f76e7-c316-481b-beac-fb5ca3e6519d'
                            , '77e3c160-2133-4268-b010-ce8e5262f99a']}


yandex_address = {}
yandex_address_id = 1

cursor_in.execute(query)

start_time = time.time()

for row in cursor_in:

    address = row.get('value')
    id = row.get('id')

    print(id)

    url_loc = 'https://geocode-maps.yandex.ru/1.x'
    params_loc = {'apikey': yandex_key.get('true'),
                  'geocode': address,
                  'format': 'json',
                  # 'text': name + ',' + ' ' + city,
                  # 'type': 'biz',
                  'lang': 'ru-RU',
                  # 'results': '500',
                  }

    req = requests.get(url_loc, params=params_loc)
    res = json.loads(req.text)

    if req.status_code != 403:

        try:
            for obj in res.get('response').get('GeoObjectCollection').get('featureMember'):
                yandex_address['id_address'] = id
                yandex_address['value'] = str(obj.get('GeoObject').get('metaDataProperty').get('GeocoderMetaData').get('Address'))
                yandex_address['id'] = yandex_address_id

                cursor_out.execute(query_yandex_address, yandex_address)
                cnx_out.commit()

                yandex_address_id += 1
                # print(yandex_address['id'], yandex_address['value'])
        except AttributeError:
            yandex_address['id_address'] = id
            yandex_address['value'] = str('Empty')
            yandex_address['id'] = yandex_address_id

            cursor_out.execute(query_yandex_address, yandex_address)
            cnx_out.commit()

            yandex_address_id += 1

        cursor_out.execute(query_done, row)
        cnx_out.commit()
    else:
        break
# print(json.dumps(res, sort_keys=True, indent=4, separators=(',', ': ')))

print("--- %s seconds ---" % (time.time() - start_time))
