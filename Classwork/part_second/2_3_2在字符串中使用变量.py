first_name='ada'
last_name='lovelace'

full_name=f'{first_name}{last_name}' #f''，f意为format，即字符串
print(full_name)

print(f'Hello, {full_name.title()}!') #Hello, Adalovelace!

message=f'Hello, {full_name.title()}!'
print(message)