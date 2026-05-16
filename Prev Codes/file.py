def r(a):
	file=open(a,'r')
	print(file.read())
def w(a):
	file=open(a,'w')
	b=input('Enter what to write: ')
	file.write(b)
def app(a):
	file=open(a,'a')
	b=input('Enter what to append: ')
	file.write(b)

