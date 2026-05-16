import re
pattern=r"^[\w._%+-]+@[\w._]+\.[\w]{2,}$"
a=input('Enter the email:')
x=re.match(pattern,a)
if x:
	print('valid email')
else:
	print('invalid email')
