myDict = {'key': ['good']}
try:
    for obj in myDict.get('key') or 'Empty':
        print(obj)
except AttributeError:
    print('Empty')
