import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
host="172.16.28.156"
port=8765
s.bind((host,port))
s.listen(3)
connection,adress=s.accept()
print(f'Server is connected with adress: {adress}')
m={'hi':'hello','how are you?':'fine','syllabus complete?':'no!!'}
while True:
	connection.sendall('Enter a message: '.encode('utf-8'))
	message=connection.recv(1024)
	msg=message.decode('utf-8')
	if msg==' ':
		connection.sendall(' '.encode('utf-8'))
		break
	if msg not in m:
		connection.sendall('Sorry cannot reply'.encode('utf-8'))
	else:
		connection.sendall(m[msg].encode('utf-8'))
connection.sendall('Thanks'.encode('utf-8'))
connection.close()
