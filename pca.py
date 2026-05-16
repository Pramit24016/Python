import re
l=[]
log=r"\b[A-Z]+[^\s]\b"
time=r"(\d\d\d\d-\d\d-\d\d\s\d\d:\d\d:\d\d)"
message=r"-\s(\w+[\sa-z]+)"
a=input('Enter the file name:')
file=open(a,'r')
b=file.read()
x=re.findall(log,b)
y=re.findall(time,b)
z=re.findall(message,b)
count=1
for i,j,k in zip(x,y,z):
	dict={}
	dict['log level']=i
	dict['timestamp']=j
	dict['message']=k
	l.append(dict)
for i in l:
	print(i)
