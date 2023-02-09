"Знак равенства"
# print (5==5) -> True
# print (5==4) -> False

# "=" -> знак присвоения
# "==" -> знак сравнения
# "!=" -> знак НЕравенства. 

"Знак больше "
# print (5 > 5) -> # False
# print (5 > 4) -> # True

"знак меньше"
# print (5<4) -> False
# print (5<10) -> True 

"Больше или равно"
# print (5>=10) -> False
# print (5>=5)  -> True


"меньше или равно"
# print (5<=3) -> False
# print (10<=15) -> True 

# print ('5'==5) -> False
# print ('hello' == 'hello') -> True
# print ("Hello" == "hello") -> False


"_______AND OR NOT_______"
# and - и 
# or - или
# not - НЕ

"__AND__"
# print (a == 5 and b ==6) -> True
#print (a==5 and b ==5 ) -> False



"__OR__"
# print ( a==4 or b == 3) -> False
# print (a ==5 or b ==4 ) -> True

"__not__"
# a = 5 
# b = 7

# print (not a == 5) -> False
# print (not a == 3 or not b == 7) -> True
# print (not a == 3 and not b == 7) -> True
# print (not True) ->  False
# print (not False) -> True 

"____________Boolean Type____________"
# булевый тип имеет два значения: 1)True и 2)False 
# print (bool(1)) -> True
# print (bool(0)) -> False
# print (bool(-11)) -> True

# print (bool('hello')) -> True
# print (bool(' ')) -> True
# print (bool('')) -> False

# print (bool([])) -> False
# print (bool([[]])) -> True

"______None Type______"
# None - неизменяемый тип данных с одним значением None,
# который используется для обозначения пустоты. 
# print (bool(None)) -> False
# print (bool ('None')) -> True

"______Условные операторы_______"
# Условные операторы - конструкция, которая используется для того, чтобы 
# при разных входных данных код работал по-разному (в зависимости от условия.)

4


# В одной конструкции мы можем использовать только один if 
# в одной конструкции мы можем использовать неограниченное
# количество elif или не использовать вообще. 

# в одной конструкции мы можем использовать только один
# else или не использовать вообще. 

# num = int(input('Введите число: '))
# if num > 0:
#     print (f'число {num} - положительное')
# elif num == 0:
#     print(f'число {num} - это 0 ')
# else: 
#     print (f'число {num} - отрицательное')


# password = input('Придумайте свой пароль: ')
# upper_let = password[0].upper()

# if len(password) <= 8:
#     print('Ваш пароль меньше 8 символов')

# elif not password.startswith(upper_let):
#     print('Ваш пароль не начинается с большой буквы')

# else:
#     print('Успешно создан пароль')

"___________Тернарные операторы______________"
# Тернарные операторы - условие в одну строку. 
# тело1 if условие else тело 2
# НЕЛЬЗЯ использовать elif в тернарных операторах.




# "_____________FizzBuzz_____________"
# num = int(input('Введите число: '))
# if num % 3 == 0 and num % 5 == 0: 
#     print ("BuzzFizz")
# elif num % 5 == 0:
#     print ('Buzz')
# elif  num % 3 == 0:
#     print ('Fizz')
# else: 
#     print (num)




