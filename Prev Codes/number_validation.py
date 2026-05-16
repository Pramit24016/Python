import re
pattern=r"^[6789]+[\d]{9}$"
a=input('Enter the number:')
x=re.match(pattern,a)
if x:
	print('Valid number')
else:
	print('Invalid number')
