"___________Словари___________"
# dict - изменяемый тип данных, итерируемый тип данных, неупорядоченный тип данных, неиндексируемый тип данных, для хранения данных в парах (ключ:значение)


# ключи в словаре всегда будут уникальными, поэтому если в словарь добавить значение по уже существующему ключу, то сохранится последнее значение. 

# dict1 = {'a':1, 'b':2, 'a':3}

# ключами могут быть только хешируемые  типы данных (неизменяемые типы данных)
# dict2 = {
#     105:'some value',
#     'key1':'some valu 2',
#     (1,2,3):'some val3',
#     None: 'Some val 4 ',
#     True: 'some val 5',
# }
# print(dict2[105])

# dict3 = {
#     'hello':[1,2,3]
# }
# print (dict3['hello'])

# dict1 = {'a':1, 'b':2,'c':3}
# print(dict1['d']) # KeyError: 'd'


"______________Создание словарей______________"
# dict1 = {'a':1, 'b':2,'c':3}

# dict2 = dict([('a',1),('b',2)])
# # {'a':1, 'b':2}


# list1 = ['a','b','c']
# list2 = [1,2,3]
# dict3 = dict(zip(list1,list2))
# {'a':1, 'b':2,'c':3}


# dict4 = {}
# dict4['name'] = 'Nastya'
# dict4['last_name'] = 'Tuz'
# print(dict4) # {'name': 'Nastya', 'last_name': 'Tuz'}


"_________Методы словаря_________"
# get - метол, который принимает в себя ключ. 
# если такой ключ есть - возвращает его значение. Если такого ключа нет - возвращает None (или default значение)

# user  = {
#     'name' : 'Nastya',
#     'age' : 13,
#     'last_name': 'Tuz'
# }
# user.get('name') #Nastya
# (user.get('id')) # None
# user.get('id',default = 10) #10
# user.get('age',default = 20) #13
#default (значение по умолчанию) - возвращается, если ключа нет. если есть ключ, возвращается его значение. 

# pop - метод, который принимает ключ, удаляет пару под этим ключом. Возвращает удалённое значение.

# dict1 = {'a':10, 'b':20, 'c':30}
# deleted = dict1.pop('a')
# print(dict1) # {'b': 20, 'c': 30}
# print(deleted) # 10

#popitem - метод, который удаляет пару, которая была добавлена последней в словарь.
# dict1 = {'a':10, 'b':20, 'c':30}
# res = dict1.popitem()
# print(dict1) # {'a': 10, 'b': 20}
# print(res) # ('c', 30)

# update - расширяет словарь, вторым словарём. 
# dict1 = {'a':1}
# dict2 = {'b':2}
# dict1.update(dict2)
# print(dict1) # {'a': 1, 'b': 2}
# print(dict2) # {'b': 2}


"____________keys,values,items____________"
# keys - возвращает список ключей
# values - возвращает список значений. 
# items - возвращает список из пар (ключ, значение)

# user  = {
#      'name' : 'Nastya',
#      'age' : 13,
#      'last_name': 'Tuz'
#  }

# print(user.values()) # dict_values(['Nastya', 13, 'Tuz'])

# print(user.items()) # dict_items([('name', 'Nastya'), ('age', 13), ('last_name', 'Tuz')])

"___________-Итерирование словарей___________-"
user  = {
      'name' : 'Nastya',
      'age' : 13,
      'last_name': 'Tuz'
  }

# for i in user: # когда проходимся по словарю - получаем ключи.
#     print(i)
# name
# age
# last_name

# for i in user.keys():
#     # когда итерируем dict_keys - проходимся по ключам
#     print(i)
# name
# age
# last_name

# for i in user.values():
#     # когда итерируем dict_values - проходимся по значениям.
#     print(i)
# Nastya
# 13
# Tuz

# for i in user.items():
#     # когда итерируем dict_values - проходимся по значениям.
#     print(i)
# ('name', 'Nastya')
# ('age', 13)
# ('last_name', 'Tuz')

# for key, value in user.items():
#     print(key) #name
#     print(value) #Nastya


# dict1 = {'a':1, 'b':2, 'c':3}
# res = {}
# for key, value in dict1.items():
#     res[value] = key
# print(res)

# создать новый словарь, где ключами будут значения из dict1, а значениями ключи из dict1
# res = {1:'a', 2:'b',3:'c'}

dict11 = {
    'a':{'key':1},
    'b':{'key':2},
    'c':{'key':3},
}
res = {}
for key, inner_dict in dict11.items():
    res[key] = inner_dict['key']
print(res)

# res = {"a":1, "b":2, "c":3}












