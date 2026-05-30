import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
host="172.16.28.156"
port=8765
s.connect((host,port))
while True:
	x=s.recv(1024).decode('utf-8')
	a=input(x)
	s.sendall(a.encode('utf-8'))
	b=s.recv(1024).decode('utf-8')
	if b==' ':
		break
	else:
		print('\n'+b)
print(s.recv(1024).decode('utf-8'))
s.close()
