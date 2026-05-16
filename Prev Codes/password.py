import re
pattern=r"^[\w?_*&^%$#@!/|]{8,}$"
a=input("Enter the password:")
strong=r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&_><?/]).*"
x=re.match(pattern,a)
if x:
	print('Valid password')
	y=re.match(strong,a)
	if y:
		print('Strong Password')
else:
	print('Invalid Password')
