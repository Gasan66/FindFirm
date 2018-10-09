myDict = {}
try:
    for obj in myDict.get('key').get('test') or 'Empty':
        print(obj)
except AttributeError:
    print('Empty')
