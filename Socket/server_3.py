mport socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
host="172.16.28.156"
port=8766
s.bind((host,port))
s.listen(3)
connection,adress=s.accept()
print(f'Server is connected with adress: {adress}')
count=0
while True:
	count+=1
	a=s.recv(1024).decode('utf-8')
	if a==1:
		file=s.recv(10240).decode('utf-8')
		f_name='upload_'+count
		f=open(f_name,'w')
		f.write(file)
	elif a==2:
		f_name=s.recv(1024).decode('utf-8')
		try:
			f=open(f_name,'rb')
			
