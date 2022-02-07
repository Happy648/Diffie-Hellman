import socket			
import time
s = socket.socket()		

port = 12345			

s.connect(('127.0.0.1', port))
P=int(s.recv(1024).decode())
G=int(s.recv(1024).decode())
Xb=int(input("Enter value for Xb:"))
Yb=pow(G,Xb)%P
print("Yb value is:",Yb)
Ya=int(s.recv(1024).decode())
time.sleep(0.5)
s.send(str.encode(str(Yb)))
Skey=pow(Ya,Xb)%P
print("The Secret Key is:",Skey)
print (s.recv(1024).decode())
s.close()	
	


