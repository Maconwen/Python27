"=========Числа=========="

#int - целые числа 
a = 5
print(type(a)) 

b = "5"
print(type(b)) # <class "str">

c = int('10')
print(type(c)) # <class "int">
# int ("5a")
# ValueError: invalid literal for int () with base 10: "5a" 

# float - числа с плавающей точкой (дробные)

a = 10.5 
print(type(a))  #<class "float">

b = float("15.3")
print(type(b))  #<class "float"> 

c = float(11)
print(c) #11.0

print (0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1)
#0.9999999999999999


#decimal - точное дробное число, нужно передавать в строковом значении ("")
#чтобы его использовать, нужно его импортировать. 
from decimal import Decimal
a = Decimal (0.1) #мы уже передали НЕ точное число
print(a+a+a+a+a+a+a+a+a+a)
#1.000000000000000055511151231

b = Decimal('0.1') 
print(b+b+b+b+b+b+b+b+b+b)
#1.0

#bin - бинарные числа
a = bin(10)
print(a) #0b1010
b = int(a,2)
print(b) #10

#hex - 16 система счисления
a = hex(15)
print(a) #0xf
b = int(a,16)
print(b) #15

#complex - комплексные числа (3i+5j-7k+10)
a = complex(10,3)
print(a) # (10+3j)


"==================Операции над числами=================="
# 5 + 7 сложение 
# 10 - 4 вычитание
# 10 * 3 умножение 
# 10 / 5 = 2.0 деление 
# 10 // 5 = 2 целочисленное деление 
# 5 % 2 = 1 это остаток от деления
# 2 ** 3 = 8 возведение в степень. (8 = 2*2*2) 
# 25 ** 0.5 = 5 нахождение квадратного корня от числа. 


# модуль числа - из отрицательного в положительное. 
abs(5) #5
abs(10) #10
abs(35)

# pow состоит из 2-3 чисел. 1 число возводится в степень 2го числа, 3ее число находит остаток
# 1. возводит в степень 
# 2. находит остаток от деления на 3 число. 
pow(2,3) #8 = 2*2*2 = 2**3
pow(2,3,4) #0 = (2*2*2)%4


# divmod 
# 1 число - целочисленное деление 
# 2 число - остаток от деления. 
res = divmod(5,2) 
print(res)  # (2,1)

# 2 = 5 // 2
# 1 = 5 % 2

divmod(17,3) # (5,2)
# 5 = 17 // 3 
# 2 = 17 % 3

#sqrt - нахождение квадратного корня,  нужно импортировать
from math import sqrt
sqrt(25)  #5
sqrt(9) #3
sqrt(3) #1.7320508075688772


seconds_in_minute = 60
minutes_in_hour = 60 
seconds_in_hour = seconds_in_minute * minutes_in_hour
hours_in_day = 24
seconds_in_day = seconds_in_hour * hours_in_day
days_in_months = 30
seconds_in_month = seconds_in_day * days_in_months
months_in_year = 12
seconds_in_year = seconds_in_month * months_in_year
print (seconds_in_year)