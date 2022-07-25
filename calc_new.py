
def input_value():
		x = None
		while type(x)!=int and type(x)!=float:
			x = input('Введите значение')	
			if ',' in x:
				x1 = x.replace(',','.')
				x = x1	
			if '.' in x:
				try:
					x = float(x)
				except:
					print('Вы ввели не число')
			else:
				try:
					x = int(x)
				except:
					print('Вы ввели не число')
		return x
				
while True:	
	a = input_value()
	b = input_value()
	
	x = None
	while x !='+' and x !="-" and x !='/' and x !='*':
		x = input('Введите +,-,/ или *')
		if x == '+':
			print(a+b)
		elif x == '-':
			print(a-b)
		elif x == '/':
			try:
				print(a/b)
			except ZeroDivisionError:
				print('Деление на ноль невозможно')
		elif x == '*':
			print(a*b)
		else:
			print('введите +,-,/,*')
	
	print('Для выхода из калькулятор нажмите "q". Для продолжения работы нажмите любой другой символ')
	y = str(input())
	if y == 'q':
		break
