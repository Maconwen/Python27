# "____________________List____________________"
# # список - это изменяемый, итерируемый, индексируемый, упорядоченный тип данных, предназначенный для хранения элементов в строгом порядке. 

# list1 = [1,3.4,'stroka', [1,2,3,4.56], (1,2), None, True, False]
# list1[0] #1
# list1[3] #[1,2,3,4.56]
# list1[3][-1] #4.56 [3] - заходит в список, берёт оттуда последний элемен [-1]
# list1[-1] #False
# list1[2][-1] #a, [2] заходит в строку 'stroka', берёт оттуда последний символ (а) [-1]

# list2 = list('stroka')
# # print(list2) # ['H', 'e', 'l', 'l', 'o']
# list3 = list (range(3,10,2))
# # print(list3) # [3, 5, 7, 9]

# "_______________изменяемость_______________"
# string = 'hello'
# res = string.upper()
# print(string) # ' hello ' 
# print (res) # 'HELLO'

# list1 = []
# list1.append(1)
# list1.append('a')
# list1.append(3)
# print(list1)

"______________Методы списков______________"
# append - метод который ДОБАВЛЯЕТ элемент В КОНЕЦ списка.
# list1 = [] # литералы списков - []
# list1.append(3)
# list1.append('Hey')
# list1.append([1,2,3])
# print(list1)
# remove - метод, который УДАЛЯЕТ элемент из списка по ЗНАЧЕНИЮ, только первое вхождение. Выдаст ошибку, если элемента нет в списке.
# list2 = [10, 'hello', 500,'world', 1000, 'hello', 500]
# list2.remove('hello')
# print(list2) #[10, 500, 'world', 1000, 'hello', 500]

# # pop - метод УДАЛЯЕТ элемент из списка по ИНДЕКСУ, в случае отсутсвия индекса, выдаст IndexError
# list3 = [10,20,30,40,50]
# list3.pop() #удаление с конца
# print (list3) # [10,20,30,40]
# list3.pop(1) # удаление по индексу
# print(list3) # [10,30,40]
# # также метод pop возвращает удаленный элемент.
# list4 = ['10','20','30','40','50']
# popped = list4.pop(0)
# print (list4) # [20,30,40,50]
# print(popped) # 10 

# insert - метод ДОБАВЛЯЕТ элемент в список по ИНДЕКСУ.
# list5 = [1,2,3,4]
# list5.insert(0,'hey')
# print(list5) # ['hey',1,2,3,4]


# list1 = [1,2,3,4,5,6,7,8,9,10]
# print (list1[::-1])
# print(list(reversed (list1)))


# print (dir(list))

#clear - чистит список (полностью)
# list1 = [1,2,3,4]
# list1.clear()
# print(list1)

#count - считает кол-во элементов, к-й передается в метод в списке. 
# list1 = [1,2,3,1,4,1,2,8]
# list1.count(1) #3
# list1.count(3) #1
# list1.count('hello') #0

# list1 = ['hello','hello','hello']
# list1.count('hello') #3
# list1.count('l') #0
# print(list1.count('hello'))

# index - возвращает индекс указанного элемента. 
# list13 = ['Hello', 'world', 'makers']
# ind = list13.index('makers')
# print(ind)

# sort  - метод, сортирует по возрастанию, если передать .sort(reverse=true) - будет сортировать по убыванию. 
list3 = [34,12,67,12,89,45]
list3.sort(reverse=True) # [12, 12, 34, 45, 67, 89]
print(list3) # [89, 67, 45, 34, 12, 12]

list4 = ['a','b','c', 'A','B']
list4.sort()
print(list4) #['A', 'B', 'a', 'b', 'c']

# copy() - возвращает копию списка.
list1 = [1,2,3]
list2 = list1.copy()
list2.append(4)
print(list1)
print(list2)


# extend() - расширяет список другим списком
list1 = [1,2,3,4]
list2 = [5,6,7,8]
# list1.append(list2)
# list1 [1,2,3,4, [5,6,7,8]]
list1.extend(list2)
# list1 [1,2,3,4,5,6,7,8]
