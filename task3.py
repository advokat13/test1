#3.1 Организовать консольный вывод строки “Hello world!”
print ('Hello world!')

#3.2  + Запросить консольный ввод имени пользователя, организовать консольный вывод строки вида: “Hello, {user}!”, где user – введенное пользователем имя
user = input('Enter your name')
print ('Hello',user,'!')

#3.3 Объявить переменную строкового типа со значением ‘Hi, I am a string variable’, 
#объявить переменную с целочисленным значением 100. Организовать консольный вывод конкатенации 
#строковой и целочисленной переменных с результатом: ‘Hi, I am a string variable100’
s1='Hi, I am string variable'
a=100
text=f'{s1}{a}'
print(text)

#3.4 Организовать консольный вывод факториала от 100
import math
print (math.factorial(100))


tup = tuple(range(0,101,2))
print (tup)

tup2=[i**2 for i in tup]
print (tup2)

#В строковой переменной ‘sounds/lofi/chillstep.wav’ выполнить замену sounds на midi, выполнить вывод расширения имени файла#
str='sounds/lofi/chillstep.wav'
print (str.replace ('sounds','midi'))
print (str[-3:])



a = [1, 1, 2, 3, 5, 8, 10, 10]
a2=set(a)
print (a2)


a3=[i+1 for i in a]
print (a3)

str2='Python is the most popular programming language'
x=str2.count('P')
b=str2.count ('p')
print (x+b)

#вывести только те элементы из первого списка, которые отсутствуют во втором#
a1 = [0, 2, 3, 4] 
b1 = [2, 2, 5]
c1=set(a1) - set(b1)
print(c1)









