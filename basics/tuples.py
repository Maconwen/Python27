"___________________Кортеж___________________"
# tuple - неизменяемый, тип данных, предназначенный для хранения элементов в строгом порядке. (В целом ничем не отличается от списков, просто неизменяемый, поэтому занимает меньше памяти)

tuple1 = (1,2,3,4)
tuple2 = (5) # int
tuple3 = 1,2,3,4 # tuple
tuple4 = 5, #tuple(5)
tuple5 = (1,'hello', [2,3,4])
tuple5[-1].append(5)
# tuple5 = (1,'hello', [2,3,4,5]
##TypeError: 'tuple' object does not support item assignment
tuple6 = tuple('hello')
print(tuple6)
#('h', 'e', 'l', 'l', 'o')

"_______________Методы tuple_______________"
# count - считает количество данного элемента в tuple
tuple1 = (1,2,3,4,5,1,1,6) 
print (tuple.count(1)) # 3
print(tuple.count('hello')) #0

# index - возвращает индекс данного элемента в tuple
tuple2 = ('hello', 'world', 105)
print(tuple2.index('hello')) #0
print(tuple2.index('w')) # ValueError: tuple.index(x): x not in tuple




