import re
dic1={}
dic2={}
dic3={}
log=r"\b[A-Z]+[^\s]\b"
time=r"(\d\d:\d\d:\d\d)"
message=r"-\s(\w+\s[a-z]+)"
a=input('Enter the file name:')
file=open(a,'r')
b=file.read().splitlines()
count=1
for i in b:
	x=re.match(log,i).group()
	y=re.match(time,i).group()
	z=re.match(message,i).group()
	dic1[count]=x
	dic2[count]=y
	dic3[count]=z
	count+=1
print(dic1)
print(dic2)
print(dic3)

