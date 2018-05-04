import dgis
import requests
import json
import time


start_time = time.time()

dadata_key = {'true': '69df660da2b7ae419968a6c8ffe4108a59704d84'
              , 'other': ['69df660da2b7ae419968a6c8ffe4108a59704d84'
                          , '2f92bf65db533b1542f65ac8692b14b9cee91b45']}

yandex_key = {'true': '0cbc01a5-fe7e-4ada-b587-37f5180b5af3'
              , 'other': ['0cbc01a5-fe7e-4ada-b587-37f5180b5af3'
                          , 'aafff3ab-15a3-489a-b129-e1caf80c6c8e']}


def find_org_name(inn):

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

    if len(res_inn.get('suggestions')) != 0:
        name_org = res_inn.get('suggestions')[0].get('data').get('name').get('full')
    else:
        name_org = 'Have not found'

    return name_org


def find_org_loc(name, city):

    url_loc = 'https://search-maps.yandex.ru/v1/'
    params_loc = {'apikey': yandex_key.get('true')
                  , 'text': name + ',' + ' ' + city
                  , 'type': 'biz'
                  , 'lang': 'ru-RU'
                  , 'results': '500'}

    req = requests.get(url_loc, params=params_loc)
    res = json.loads(req.text)
    list_org = res.get('features')
    list_org_loc = []
    # print(req.url)

    for org in list_org:
        list_org_loc.append([org.get('properties').get('CompanyMetaData').get('name')
                            , org.get('properties').get('CompanyMetaData').get('address')
                            , org.get('properties').get('CompanyMetaData').get('Categories')[0].get('name')
                            , org.get('properties').get('CompanyMetaData').get('Phones')[0].get('formatted')
                            , org.get('properties').get('CompanyMetaData').get('Hours').get('text')
                            ])
    return list_org_loc


print(find_org_loc(find_org_name(3627022104), 'Воронеж'))
# print(find_org_name(361900063900))

# with open('INN.txt', 'r') as inf, open('Data_org', 'w') as ouf:
#     i = 0
#     while i < 400:
#         inn = inf.readline().strip()
#         name_org = find_org_name(inn)
#         adress_list = find_org_loc(name_org, 'Воронеж')
#         for adress in adress_list:
#             for element in adress:
#                 ouf.writelines(element + ';')
#             ouf.writelines(inn + ';' + name_org)
#             ouf.writelines('\n')
#         i += 1
#         print(i)
#
# print("--- %s seconds ---" % (time.time() - start_time))



















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
