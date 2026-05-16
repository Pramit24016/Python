def new_student(l):
	a=input('Enter the student name: ')
	b=int(input('Enter the student age: '))
	c=list(map(int,input("Enter the marks: ").split()))
	l.append([a,b,c])
def cal_result(x,l):
	r=l[x][2]
	s=sum(r)
	size=len(r)
	p=(s/size)
	print('The total marks is: ',s)
	print('The percentage obtained is:',p)
def all_students(l):
	for i in l:
		print(f'Name:{i[0]} Age:{i[1]}')


