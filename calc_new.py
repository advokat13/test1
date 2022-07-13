while True:	
	
	def input_value():
		x=()
		while type(x)!=int and type(x)!=float:
			print('Введите значение')
			x=input()	
			if ',' in x:
				x1=x.replace(',','.')
				x=x1	
			if '.' in x:
				try:
					x=float(x)
				except:
					print('Вы ввели не число')
			else:
				try:
					x=int(x)
				except:
					print('Вы ввели не число')
		return x
	
	a=input_value()
	b=input_value()
	
	print('Введите +,-,/ или *')
	x=()
	while x !='+' and x !="-" and x !='/' and x !='*':
		x=input(x)
		if x=='+':
			print(a+b)
		elif x=='-':
			print(a-b)
		elif x=='/':
			try:
				print(a/b)
			except ZeroDivisionError:
				print('Деление на ноль невозможно')
		elif x=='*':
			print(a*b)
		else:
			print('введите +,-,/,*')
	
	print('Для выхода из калькулятор нажмите "q". Для продолжения работы нажмите любой другой символ')
	y=str(input())
	if y=='q':
		break
