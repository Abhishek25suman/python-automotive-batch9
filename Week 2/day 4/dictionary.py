# ---Dictionary Prodram---
#Ditionary is a changeable, unordered, collection of unique key:value pair

currencies = {'USA': 'Dollar',
              'Japan': 'Yen',
              'UK': 'Pound',
              'Europe': 'Euro'}

print(currencies['Europe'])
print(currencies.get('India'))
print(currencies.keys())
print(currencies.values())
print(currencies.items())

currencies.update({'India': 'Rupees'})
print(currencies.items())
currencies.update({'USA': 'US Dollar'})
print(currencies.items())
currencies.pop('Japan')
print(currencies.items())
currencies.clear()

for key, value in currencies.items():
    print(key, value)