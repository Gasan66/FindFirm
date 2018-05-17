import dgis
import requests
import json
import time


start_time = time.time()

dadata_key = {'true': 'aa6a9d82918d359141ce243817d31c8150f05124'
              , 'other': ['aa6a9d82918d359141ce243817d31c8150f05124'
                          , '2f92bf65db533b1542f65ac8692b14b9cee91b45'
                          , '8e574e1a8c1a8aa48102384664b3b75cd6298b95'
                          , 'b2eaa3e02e171719b74ad1d7cee66e98ddf68c4c'
                          , '66c1134b2bc391c25495e6ae1f709c6a56886ba8'
                          , 'a131f0b77943c492f52126d6374400ff5619fc40'
                          , '770075713890b9075ac4c100444da1448d9e8e65']}

yandex_key = {'true': 'aafff3ab-15a3-489a-b129-e1caf80c6c8e'
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


def find_org_requisites(inn):

    requisites = []

    isKeyGood = False

    while isKeyGood is False:

        url_inn = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party'
        headers = {'Authorization': 'Token' + ' ' + dadata_key.get('true')
                   , 'Content-Type': 'application/json'
                   , 'Accept': 'application/json'}
        data = {'query': inn}

        req_inn = requests.post(url_inn, data=json.dumps(data), headers=headers)
        res_inn = json.loads(req_inn.text)
        # print(res_inn)
        if res_inn.get('reason') == 'Forbidden':
            dadata_key['true'] = dadata_key.get('other')[dadata_key.get('other').index(dadata_key.get('true')) + 1]
        else:
            isKeyGood = True

    if len(res_inn.get('suggestions')) != 0:
        for suggestion in res_inn.get('suggestions'):

            dadata_name = suggestion.get('data').get('name').get('full')

            if suggestion.get('data').get('branch_type') is not None:
                dadata_branch_type = suggestion.get('data').get('branch_type')
            else:
                dadata_branch_type = 'Have not found'

            if suggestion.get('data').get('branch_count') is not None:
                dadata_branch_count = suggestion.get('data').get('branch_count')
            else:
                dadata_branch_count = 'Have not found'

            if suggestion.get('data').get('name').get('full_with_opf') is not None:
                dadata_name_full_with_opf = suggestion.get('data').get('name').get('full_with_opf')
            else:
                dadata_name_full_with_opf = 'Have not found'

            if suggestion.get('data').get('name').get('short_with_opf') is not None:
                dadata_name_short_with_opf = suggestion.get('data').get('name').get('short_with_opf')
            else:
                dadata_name_short_with_opf = 'Have not found'

            if suggestion.get('data').get('name').get('short') is not None:
                dadata_name_short = suggestion.get('data').get('name').get('short')
            else:
                dadata_name_short = 'Have not found'

            if suggestion.get('data').get('address').get('value') is not None:
                dadata_address_value = suggestion.get('data').get('address').get('value')
            else:
                dadata_address_value = 'Have not found'

            if suggestion.get('data').get('address').get('unrestricted_value') is not None:
                dadata_address_unrestricted_value = suggestion.get('data').get('address').get('unrestricted_value')
            else:
                dadata_address_unrestricted_value = 'Have not found'

            if suggestion.get('data').get('address').get('data') is not None:
                if suggestion.get('data').get('address').get('data').get('geo_lat') is not None:
                    dadata_address_geo_lat = suggestion.get('data').get('address').get('data').get('geo_lat')
                else:
                    dadata_address_geo_lat = 'Have not found'
            else:
                dadata_address_geo_lat = 'Have not found'

            if suggestion.get('data').get('address').get('data') is not None:
                if suggestion.get('data').get('address').get('data').get('geo_lon') is not None:
                    dadata_address_geo_lon = suggestion.get('data').get('address').get('data').get('geo_lon')
                else:
                    dadata_address_geo_lon = 'Have not found'
            else:
                dadata_address_geo_lon = 'Have not found'

            if suggestion.get('data').get('opf') is not None:
                dadata_opf = suggestion.get('data').get('opf').get('short')
            else:
                dadata_opf = 'Have not found'

            if suggestion.get('data').get('okved') is not None:
                dadata_okved = suggestion.get('data').get('okved')
            else:
                dadata_okved = 'Have not found'

            requisites.append({'name': dadata_name
                              , 'name_short': dadata_name_short
                              , 'branch_type': dadata_branch_type
                              , 'branch_count': dadata_branch_count
                              , 'opf': dadata_opf
                              , 'name_full_with_opf': dadata_name_full_with_opf
                              , 'name_short_with_opf': dadata_name_short_with_opf
                              , 'address_value': dadata_address_value
                              , 'address_unrestricted_value': dadata_address_unrestricted_value
                              , 'address_geo_lat': dadata_address_geo_lat
                              , 'address_geo_lon': dadata_address_geo_lon
                              , 'okved': dadata_okved})
    else:
        requisites = 'Have not found'
    return requisites


def find_org_loc(name, city):

    isKeyGood = False

    while isKeyGood is False:

        url_loc = 'https://search-maps.yandex.ru/v1/'
        params_loc = {'apikey': yandex_key.get('true')
                      , 'text': name + ',' + ' ' + city
                      , 'type': 'biz'
                      , 'lang': 'ru-RU'
                      , 'results': '500'}

        req = requests.get(url_loc, params=params_loc)
        res = json.loads(req.text)

        if res.get('message') == 'invalid key':
            yandex_key['true'] = yandex_key.get('other')[yandex_key.get('other').index(yandex_key.get('true')) + 1]
        else:
            isKeyGood = True

    list_org = res.get('features')
    if list_org is None:
        list_org_loc.append(['Have not found', 'Have not found', 'Have not found', 'Have not found', 'Have not found', 'Have not found',])
        return list_org_loc
    list_org_loc = []
    # print(req.url)

    for org in list_org:
        yandex_name = org.get('properties').get('CompanyMetaData').get('name')
        yandex_address = org.get('properties').get('CompanyMetaData').get('address')
        yandex_categories = org.get('properties').get('CompanyMetaData').get('Categories')
        yandex_phones = org.get('properties').get('CompanyMetaData').get('Phones')
        yandex_hours = org.get('properties').get('CompanyMetaData').get('Hours')
        yandex_coordinates = org.get('geometry').get('coordinates')
        list_org_loc.append([yandex_name, yandex_address, yandex_categories, yandex_phones, yandex_hours, yandex_coordinates])
    return list_org_loc


with open('TrueINN', 'r') as inf, open('Data_Main', 'w') as main_ouf, open('Data_Filial', 'w') as filial_ouf:

    main_ouf.writelines('NameDadata' + ';' +
                        'NameDadataShort' + ';' +
                        'NameYandex' + ';' +
                        'address' + ';' +
                        'Categories' + ';' +
                        'Phone' + ';' +
                        'Availability' + ';' +
                        'Coordinates' + ';' +
                        'INN' + ';' +
                        'OKVED' + ';' +
                        'OPF' +
                        'City' + '\n')

    filial_ouf.writelines('NameDadata' + ';' +
                          'NameDadataShort' + ';' +
                          'INN' + ';' +
                          'Branch_type' + ';' +
                          'Branch_count' + ';' +
                          'OPF' + ';' +
                          'Name_full_with_opf' + ';' +
                          'Name_short_with_opf' + ';' +
                          'Address​_value' + ';' +
                          'Address​_unrestricted_value' + ';' +
                          'Geo_lat' + ';' +
                          'Geo_lon' +
                          'City' + '\n')
    i = 0
    while i < 50000:
        inn, city = inf.readline().split()
        # inn = '814071096'
        requisites_org = find_org_requisites(inn)
        # print(requisites_org)
        if requisites_org != 'Have not found' and len(requisites_org) > 1:
            for requisite_org in requisites_org:
                if requisite_org.get('branch_type') == 'MAIN':
                    name_org = requisite_org.get('name')
                    name_org_short = requisite_org.get('name_short')
                    opf_org = requisite_org.get('opf')
                    okved_org = requisite_org.get('okved')

                    address_list = find_org_loc(name_org, city)
                    if len(address_list) != 0:
                        for address in address_list:
                            main_ouf.writelines(name_org + ';')
                            main_ouf.writelines(name_org_short + ';')

                            if address[0] is not None:
                                main_ouf.writelines(address[0] + ';')
                            else:
                                main_ouf.writelines('Have not found' + ';')

                            if address[1] is not None:
                                main_ouf.writelines(address[1] + ';')
                            else:
                                main_ouf.writelines('Have not found' + ';')

                            if address[2] is not None:
                                for cat in address[2]:
                                    main_ouf.writelines(cat.get('name') + ',')
                                main_ouf.writelines(';')
                            else:
                                main_ouf.writelines('Have not found' + ';')

                            if address[3] is not None:
                                for tel in address[3]:
                                    main_ouf.writelines(tel.get('formatted') + ',')
                                main_ouf.writelines(';')
                            else:
                                main_ouf.writelines('Have not found' + ';')

                            if address[4] is not None:
                                main_ouf.writelines(str(address[4].get('text')).replace(';', ',') + ';')
                            else:
                                main_ouf.writelines('Have not found' + ';')

                            if address[5] is not None:
                                for coordinate in address[5]:
                                    main_ouf.writelines(str(coordinate) + ',')
                                main_ouf.writelines(';')
                            else:
                                main_ouf.writelines('Have not found')

                            main_ouf.writelines(inn + ';')
                            main_ouf.writelines(okved_org + ';')
                            main_ouf.writelines(opf_org + ';')
                            main_ouf.writelines(city)
                            main_ouf.writelines('\n')
                    else:
                        main_ouf.writelines(name_org + ';' + ('Have not found;' * 6) + inn + ';' + okved_org + ';' + opf_org + ';' + city + '\n')

                filial_ouf.writelines(requisite_org.get('name') + ';' +
                                          requisite_org.get('name_short') + ';' +
                                          inn + ';' +
                                          requisite_org.get('branch_type') + ';' +
                                          str(requisite_org.get('branch_count')) + ';' +
                                          requisite_org.get('opf') + ';' +
                                          requisite_org.get('name_full_with_opf') + ';' +
                                          requisite_org.get('name_short_with_opf') + ';' +
                                          str(requisite_org.get('address_value')).replace(';', ',') + ';' +
                                          str(requisite_org.get('address_unrestricted_value')).replace(';', ',') + ';' +
                                          str(requisite_org.get('address_geo_lat')) + ';' +
                                          str(requisite_org.get('address_geo_lon')) + ';' +
                                          city + '\n')
        elif requisites_org != 'Have not found':
            for requisite_org in requisites_org:
                name_org = requisite_org.get('name')
                name_org_short = requisite_org.get('name_short')
                opf_org = requisite_org.get('opf')
                okved_org = requisite_org.get('okved')

                address_list = find_org_loc(name_org, city)
                if len(address_list) != 0:
                    for address in address_list:
                        main_ouf.writelines(name_org + ';')
                        main_ouf.writelines(name_org_short + ';')

                        if address[0] is not None:
                            main_ouf.writelines(address[0] + ';')
                        else:
                            main_ouf.writelines('Have not found' + ';')

                        if address[1] is not None:
                            main_ouf.writelines(address[1] + ';')
                        else:
                            main_ouf.writelines('Have not found' + ';')

                        if address[2] is not None:
                            for cat in address[2]:
                                main_ouf.writelines(cat.get('name') + ',')
                            main_ouf.writelines(';')
                        else:
                            main_ouf.writelines('Have not found' + ';')

                        if address[3] is not None:
                            for tel in address[3]:
                                main_ouf.writelines(tel.get('formatted') + ',')
                            main_ouf.writelines(';')
                        else:
                            main_ouf.writelines('Have not found' + ';')

                        if address[4] is not None:
                            main_ouf.writelines(str(address[4].get('text')).replace(';', ',') + ';')
                        else:
                            main_ouf.writelines('Have not found' + ';')

                        if address[5] is not None:
                            for coordinate in address[5]:
                                main_ouf.writelines(str(coordinate) + ',')
                            main_ouf.writelines(';')
                        else:
                            main_ouf.writelines('Have not found')

                        main_ouf.writelines(inn + ';')
                        main_ouf.writelines(okved_org + ';')
                        main_ouf.writelines(opf_org + ';')
                        main_ouf.writelines(city)
                        main_ouf.writelines('\n')
                else:
                    main_ouf.writelines(
                        name_org + ';' + ('Have not found;' * 6) + inn + ';' + okved_org + ';' + opf_org + ';' + city + '\n')
        else:
            main_ouf.writelines(('Have not found;' * 7) + inn + ';' + ('Have not found;' * 2) + ';' + city +'\n')
        i += 1
        print(i)

print("--- %s seconds ---" % (time.time() - start_time))
