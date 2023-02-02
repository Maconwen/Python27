"______________Строки______________"
# строки - это неизменяемый тип данных, предназначенный для хранения текста (последовательности символов)

string1 = 'строка в одинарных кавычках'
string2 = "строка в двойных кавычках"
string3 = "Don't"
string4 = 'Study in "MakersIncubator"'
string5 = """
МНогострочный 
текст
тут можно использовать 'любые' "кавычки"
"""

string7 = 'hello' + '' 'world' #hello world
string8 = 'hello' *3 #hellohellohello
string9 = 'hello' + str(1)




"___________________Экранизация строк___________________"
print ('hello\nworld') 
'\n' #перенос на новую строку 
'\t' # отступ, (TABуляция)
'\\' # отображение одного \, один выступает в кач-ве экранизации. 
'\'' # отображение кавычки '
"\"" # отображение двойной кавычки "
"\r" # перенос каретки (указателя) в начало строки
"\v" # перенос на новую строку со смещением вправо на длину предыдущей строки. 

'hello\nworld' 
#hello
#world

'hello\tworld' #hello   world

'экранизация \\'
# экранизация \

'123456789\rhello'
#hello6789

'hello\vworld\vmakers'
#hello 
      #world  
             #makers

"_____________________Индексация_____________________"
# индекс - порядковый номер символа в строке (начиная с нуля)
"h e l l o"
#0 1 2 3 4

string = "hello world"
string [0] # h
string [-1] # d
string [5] # ''


#срезы - подстрока, часть строки. 
string[6:9] # "wor" 
string[0:5] # "hello"
string[0:6] # "hello "
string[:6]  # 'hello '
string[7:]  # 'orld'
string[:]   # 'hello world'
string[:11:2] # 'hlowrd'
string[::2] # 'hlowrd'
string [::-1] #

"_______________форматирование строк_______________"
title = 'Cake'
price = 35
string = f'Название {title}, цена: {price}'
print(string)
# Название Cake, цена: 35

format1 = "Название: %s, цена: %s "
print(format1 %('Яблоко', '80'))
# Название: Яблоко, цена: 80 

format2 = 'Название {}, цена: {}'
print(format2.format('Груша', 60))
# Название: Груша, цена: 60


"_________________Методы строк_________________"
# метод - функция, к-я принадлежит определённому типу данны, обращаемся к ней через точку.

(dir(str)) # посмотреть все доступные методы для данного типа данных.
'Hello'.upper() # 'HELLO'
'HELLO'.lower() # 'hello'

'hello WORLD' .swapcase() #HELLO world
'HeLLo'.swapcase() #hEllO
"hello world".title() #Hello World
'hello world'.capitalize() #Hello world

'hello'.center(11) #    hello   
print('hello'.center(11,'-')) # '---hello---'

'hello'.count('l') #2
'hello'.count('ll')  #1
'Hello'.count('hello') #0
'hello'.count('') #6


'hello world'.split() # ['hello', 'world']
'hello world'.split('o') # ['hell', 'w', 'rld']

' '.join(['hello', 'world']) # 'hello world'
'%'.join(['hello', 'world']) # 'hello%world'

'hello world'.find(w) # 6
'hello world'.find(wor) # 6
'hello world'.rfind(o) #7