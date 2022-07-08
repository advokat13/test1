#4.1 Имеется список a = list(range(0, 11)). На основании списка ‘a’ cгенерировать список, 
#каждым элементом которого является словарь, ключем которого является элемент списка ‘a’, 
#а значением квадрат ключа. ([{0:0}, {1:1}, {2:4}, etc…])

a=list(range(0,11))
a1=[]
for i in a:
	a1.append({i:i**2})
print(a1)


#4.2 Имеется словарь d1 = {‘a’: 1} и словарь d2 = {‘b’: 2} необходимо обновить значение ключа ‘b’ словаря ‘d2’ с 2 на 5. 
#Вывести словарь ‘d3’, представляющий из себя содержимое словаря ‘d1’ и ‘d2’.

d1={'a':1}
d2={'b':2}
d2['b']=5
d3=d1|d2
print(d3)


#4.3 Имеется словарь d1 = {‘key1’: 1, ‘key2’: 2}, в нем необходимо сменить ключи и значения местами, заменив ‘key’ на ‘value’ ({1: ‘value1’, 2: ‘value2’})

d1={'key1':1,'key2':2}
d_new= dict((val, key) for (key, val) in d1.items())
d_new[1]='value1'
d_new[2]='value2'
print(d_new)

#4.4 вывести список файлов из текущей директории.
import os
print(os.listdir())

#4.5 Организовать вывод текущего времени и даты в формате “hh-mm MM-dd-YYYY”
from datetime import datetime
print(datetime.now().strftime('%H:%M %d-%m-%Y'))

#4.6 Организовать последовательный вывод чисел от 0 до 10 с запросом нажатия клавиши enter пользователем для каждого последующего элемента.

for i in range(11):
	print(i)
	input('Чтобы продолжить, нажмите enter')
	
#4.7* Очистить строку string = 'LthHJKiHs GisH nKSiDJceFJ KASsolDIUKuJHtDHiSSonAK'  от заглавных букв. Вывод организовать в новой строке. 
#Пробелы так же должны содержаться в результате.

string='LthHJKiHs GisH nKSiDJceFJ KASsolDIUKuJHtDHiSSonAKL'
print(string)
string2 = ''.join(i for i in string if not i.isupper())
print(string2)


#4.8 Из списка с цветами радуги организовать консольный вывод строки вида: “Красный – 1 цвет радуги”. 
#Список цветов радуги colors = [“красный”, “оранжевый”, “желтый”, “зеленый”, “голубой”, “синий”, “фиолетовый”]. Название цвета выводить с заглавной буквы.
colors = ['красный', 'оранжевый', 'желтый', 'зеленый', 'голубой', 'синий', 'фиолетовый']
for i in colors:
	ind=colors.index(i)+1
	print(str.capitalize(i),'-',ind,'цвет радуги')


#4.9 Организовать цикл while, который будет выполнять вывод чисел от 0 до бесконечности в течении 10 секунд. 

import time


a=0
time_end = time.time() + 10
while time.time() < time_end:
	print(a)
	a=a+1


#4.10 При помощи цикла for организовать консольный вывод вида:
1
22
333
4444
55555
666666
7777777
88888888
999999999

	
for i in range(1,10):
		a=str(i)
		print(a*i)
			



