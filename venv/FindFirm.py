import dgis
import requests
import json
import time


start_time = time.time()

dadata_key = {'true': 'aa6a9d82918d359141ce243817d31c8150f05124'
              , 'other': ['aa6a9d82918d359141ce243817d31c8150f05124'
                          , '2f92bf65db533b1542f65ac8692b14b9cee91b45']}

yandex_key = {'true': 'aafff3ab-15a3-489a-b129-e1caf80c6c8e'
              , 'other': ['0cbc01a5-fe7e-4ada-b587-37f5180b5af3'
                          , 'aafff3ab-15a3-489a-b129-e1caf80c6c8e'
                          , 'b8f5a7f2-9a0c-4aa6-ab3f-5681ff78ff67'
                          , '786386b9-13e7-4526-ac14-885cbbab24ae'
                          , '11c449dc-8e6b-4a01-84d0-066975266334'
                          , 'f2106ce9-2cc7-4a12-9be4-5f7129fbcd5b'
                          , 'c0bdf248-ac07-4aaf-9774-50799f79d66d']}


def find_org_requisites(inn):

    isKeyGood = False

    while isKeyGood == False:

        url_inn = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party'
        headers = {'Authorization': 'Token' + ' ' + dadata_key.get('true')
                   , 'Content-Type': 'application/json'
                   , 'Accept': 'application/json'}
        data = {'query': inn
                , 'branch_type': 'MAIN'}

        req_inn = requests.post(url_inn, data=json.dumps(data), headers=headers)
        res_inn = json.loads(req_inn.text)

        if res_inn.get('reason') == 'Forbidden':
            dadata_key['true'] = dadata_key.get('other')[dadata_key.get('other').index(dadata_key.get('true')) + 1]
        else:
            isKeyGood = True
    # print(res_inn)
    if len(res_inn.get('suggestions')) != 0:
        name_org = [res_inn.get('suggestions')[0].get('data').get('name').get('full'),
                    res_inn.get('suggestions')[0].get('data').get('opf').get('short'),
                    res_inn.get('suggestions')[0].get('data').get('okved')]
    else:
        name_org = 'Have not found'
    # print(name_org)
    return name_org


def find_org_loc(name, city):

    isKeyGood = False

    while isKeyGood == False:

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
    list_org_loc = []
    # print(req.url)

    for org in list_org:
        yandex_name = org.get('properties').get('CompanyMetaData').get('name')
        yandex_adress = org.get('properties').get('CompanyMetaData').get('address')
        yandex_categories = org.get('properties').get('CompanyMetaData').get('Categories')
        yandex_phones = org.get('properties').get('CompanyMetaData').get('Phones')
        yandex_hours = org.get('properties').get('CompanyMetaData').get('Hours')
        yandex_coordinates = org.get('geometry').get('coordinates')

        list_org_loc.append([yandex_name, yandex_adress, yandex_categories, yandex_phones, yandex_hours, yandex_coordinates])
        # list_org_loc.append([org.get('properties').get('CompanyMetaData').get('name')
        #                     , org.get('properties').get('CompanyMetaData').get('address')
        #                     , org.get('properties').get('CompanyMetaData').get('Categories')[0].get('name')
        #                     , org.get('properties').get('CompanyMetaData').get('Phones')[0].get('formatted')
        #                     , org.get('properties').get('CompanyMetaData').get('Hours').get('text')])
    return list_org_loc
#
#
# # print(find_org_loc(find_org_name(3627022104), 'Воронеж'))
# # print(find_org_name(361900063900))

# example = [['Монтажник'
#                , 'Воронеж, Республиканская ул., 74А'
#                , [{'name': 'Монтаж и обслуживание систем водоснабжения и канализации'}
#                   , {'name': 'Сантехнические работы'}, {'name': 'Системы вентиляции'}
#                   , {'name': 'Электромонтажные работы'}]
#                , [{'type': 'phone', 'formatted': '+7 (473) 260-31-20', 'country': '7', 'prefix': '473', 'number': '2603120'}]
#                , {'Availabilities': [{'Monday': True, 'Tuesday': True, 'Wednesday': True, 'Thursday': True, 'Friday': True,
#                                       'Intervals': [{'from': '08:00:00', 'to': '17:00:00'}]}],
#                   'text': 'пн-пт 8:00–17:00',
#                   'tzOffset': 10800,
#                   'State': {'is_open_now': '1', 'text': 'Закроется в 17:00', 'short_text': 'До 17:00'}}
#             ]]


with open('INN.txt', 'r') as inf, open('Data_org_ex', 'w') as ouf:
    i = 0
    while i < 2000:
        inn = inf.readline().strip()
        # inn = '366400224362'
        requisites_org = find_org_requisites(inn)
        # print(requisites_org)
        if requisites_org is not 'Have not found':
            name_org = requisites_org[0]
            opf_org = requisites_org[1]
            okved_org = requisites_org[2]

            # name_org = 'МОНТАЖНИК'
            adress_list = find_org_loc(name_org, 'Воронеж')
            # adress_list = example
            # print(inn, name_org)
            # print(adress_list)
            if len(adress_list) != 0:
                for adress in adress_list:
                    # print(adress)
                    # for element in adress:
                    # ouf.writelines(str(adress[0]) + ';' + str(adress[1]) + ';' + str(adress[2]))
                    # ouf.writelines(inn + ';' + name_org + '\n')
                    if adress[0] is not None:
                        ouf.writelines(adress[0] + ';')
                    else:
                        ouf.writelines('Have not found' + ';')

                    if adress[1] is not None:
                        ouf.writelines(adress[1] + ';')
                    else:
                        ouf.writelines('Have not found' + ';')

                    if adress[2] is not None:
                        for cat in adress[2]:
                            ouf.writelines(cat.get('name') + ',')
                        ouf.writelines(';')
                    else:
                        ouf.writelines('Have not found' + ';')

                    if adress[3] is not None:
                        for tel in adress[3]:
                            ouf.writelines(tel.get('formatted') + ',')
                        ouf.writelines(';')
                    else:
                        ouf.writelines('Have not found' + ';')

                    if adress[4] is not None:
                        ouf.writelines(adress[4].get('text') + ';')
                    else:
                        ouf.writelines('Have not found' + ';')

                    if adress[5] is not None:
                        for coordinate in adress[5]:
                            ouf.writelines(str(coordinate) + ',')
                    else:
                        ouf.writelines('Have not found')

                    ouf.writelines(inn + ';')
                    ouf.writelines(okved_org + ';')
                    ouf.writelines(opf_org)


                # ouf.writelines(str('\n').join(map(str, adress[2].get('name'))))
                    ouf.writelines('\n')
            else:
                ouf.writelines(name_org + ';')
                ouf.writelines(inn + ';')
                ouf.writelines(okved_org + ';')
                ouf.writelines(opf_org + '\n')
        else:
            ouf.writelines('Have not found' + '\n')
        i += 1
        print(i)
#
print("--- %s seconds ---" % (time.time() - start_time))



















# print(org.get('properties').get('CompanyMetaData').keys())
# print(org.get('properties').get('CompanyMetaData').values())

# api = dgis.API('ruckdu0541')
# api.search(what=u'пиво', where=u'Иркутск')


# url_inn = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party'
# headers = {'Authorization': 'Token 69df660da2b7ae419968a6c8ffe4108a59704d84'
#            , 'Content-Type': 'application/json'
#            , 'Accept': 'application/json'}
# data = {'query': '6686100430'
#         , 'branch_type': 'MAIN'}
# params_inn = {'Authorization': 'Token 69df660da2b7ae419968a6c8ffe4108a59704d84'
#               , 'query': '6686100430'}

# req_inn = requests.post(url_inn, data=json.dumps(data), headers=headers)
# res_inn = json.loads(req_inn.text)


# url_loc = 'https://search-maps.yandex.ru/v1/'
# params_loc = {'apikey': '0cbc01a5-fe7e-4ada-b587-37f5180b5af3'
#           , 'text': 'Пивко, Нягань'
#           , 'type': 'biz'
#           , 'lang': 'ru-RU'
#           , 'results': '500'}
#
# # Запрос на яндекс
# req = requests.get(url_loc, params=params_loc)
#
# # Сохраняем овет
# res = json.loads(req.text)
# print(req.text)
#
# # Получаем список организаций
# list_org = res.get('features')
#
#
# for org in list_org:
#     # k +=1
#     print(org.get('properties').get('CompanyMetaData').get('name')
#           , org.get('properties').get('CompanyMetaData').get('address')
#           , org.get('properties').get('CompanyMetaData').get('Categories')[0].get('name')
#           , org.get('properties').get('CompanyMetaData').get('Phones')[0].get('formatted')
#           , org.get('properties').get('CompanyMetaData').get('Hours').get('text'))
# print(org.get('properties').get('CompanyMetaData').keys())
# print(org.get('properties').get('CompanyMetaData').values())
