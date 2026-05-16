def add(a,b):
	c=a+b
	return c
def subtraction(a,b):
	c=a-b
	return c
def multiplication(a,b):
	c=a*b
	return c
def division(a,b):
	try:
		c=a/b
	except ZeroDivisionError:
		print('Division by zero is not possible')
	else:
		return c

