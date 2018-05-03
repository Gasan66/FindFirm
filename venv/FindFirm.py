import dgis
import requests
import json


# api = dgis.API('ruckdu0541')
# api.search(what=u'пиво', where=u'Иркутск')


url_inn = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party'
headers = {'Authorization': 'Token 69df660da2b7ae419968a6c8ffe4108a59704d84'
           , 'Content-Type': 'application/json'
           , 'Accept': 'application/json'}
data = {'query': '6686100430'}
# params_inn = {'Authorization': 'Token 69df660da2b7ae419968a6c8ffe4108a59704d84'
#               , 'query': '6686100430'}

req_inn = requests.post(url_inn, data=json.dumps(data), headers=headers)
res_inn = json.loads(req_inn.text)
print(res_inn)


# url_loc = 'https://search-maps.yandex.ru/v1/'
# params_loc = {'apikey': 'a7478553-952d-42ca-8264-b80a07ae6341'
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
