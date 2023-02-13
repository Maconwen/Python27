'_______________Comprehensions_______________'
# генератор, с помощью которого  создавать последовательность используя цикл for 
# # list1 = []
# # for i in range(1,11):
# #     list1.append(i)
# # # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list1 = [i for i in range(1,11)]
# # print(list1) [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # результат for элемент in последовательность 
# # результат for элемент in последовательность if фильтр

# comprehension = (i for i in range(1,11))
# # print(comprehension)
# # <generator object <genexpr> at 0x7f02b69d2a50>
# # генератор - итерируемый объект, который не хранит в себе полностью все элементы последовательности, а генерирует их когда требуется.
# # print (next(comprehension))

# # next - функция, которая принимает в себя генератор, запрашивает следующий элемент у генератора и возвращает его.

# comprehension = (i for i in range(1,4))
# print(list(comprehension)) # [1,2,3]

# "___________Синтаксический сахар___________"
# # list comprehension
# list_comprehension = [i for i in 'hello']
# print(list_comprehension)
# # ['h', 'e', 'l', 'l', 'o']

# # dict comprehension 
# dict_comprehension = {i:str(i)for i in range(1,11)}
# print (dict_comprehension)
# {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10'}

# фильтр 
# string = 'Hello worlD'
# res = [i for i in string if i.islower()]
# # print (res) = ['e', 'l', 'l', 'o', 'w', 'o', 'r', 'l']
# # Этот же код можно написать в несколько строк.  
# res = []
# for i in string:
#     if i.islower():
#         res.append(i)
# print(res) = ['e', 'l', 'l', 'o', 'w', 'o', 'r', 'l']

# создать список, состоящий из чисел от 1 до 10

# list_new = [i for i in range(1,11) if i % 2 == 0]
# print(list_new)

# list_1 = [1,2,3,4,5,6,7,8,9,10]
# list_2 = []
# for i in list_1:
#     if i % 2 == 0:
#         list_2.append(i)
# print(list_2) = [2, 4, 6, 8, 10]

# res = [i for i in range(2,11,2)]
# print(res) = [2, 4, 6, 8, 10]
# for i in list_new:
#     if i % 2 == 0:
#         list_new.append(i)
# # print(list_new) = [2, 4, 6, 8, 10]

# создать список из чисел от 1 до 10, умноженные 100

# list1 = [i*100 for i in range(1,11)]
# print(list1) [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# list1 = (list(range(1,11)))
# res = []
# for i in list1:
#     res.append(i*100)
# print(res) [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]


# list1 = (list(range(100,1100,100)))
# print (list1) [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]


list3 = ['hello' for i in range(5)]
print(list3)

# users = ['test1','test2','test3']
# res = ['Hello' + name for name in users]
# res1 = [f'Hello {name}' for name in users]
# print(res1) # ['Hello test1', 'Hello test2', 'Hello test3']


# list_ = [[x for x in range(1,i+1)] for i in range(1,6)]
# print(list_)
# [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]

# dict1 = {'a':1, 'b':2, 'c':3}
# res = {v:k for k,v in dict1.items()}
# print(res)
# # {1:'a', 2:'b', 3:'c'}

# res = [[x for x in range(1,i+1)] for i in range(1,6)]


# # set comprehension 
# set_comp = {x for x in range(1,11)}
