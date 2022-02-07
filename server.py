import socket			
import time
from math import sqrt
s = socket.socket()		
print ("Socket successfully created")

port = 12345			

s.bind(('', port))		
print ("socket binded to %s" %(port))

s.listen(5)	
print ("socket is listening")		
def prime(n):
    prime_flag = 0
    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return prime_flag
        else:
            return prime_flag
    else:
        return prime_flag

def createPG():
    print("Note Prime(P) and Generator(G) are prime & P>G")
    P=int(input("Enter Prime(P):"))
    a=prime(P)
    if a==1:
        print("P is not prime")
        return 0,0,1
    G=int(input("Enter Generator(G):"))
    a=prime(G)
    if a==1:
        print("G is not prime")
        return 0,0,1
    if P<G:
        print("P is not greater than G") 
        return 0,0,1
    return P,G,0

while True:
    c, addr = s.accept()	
    print ('Got connection from', addr )
    P,G,f=createPG()
    if f==1:
        c.close()
    c.send(str.encode(str(P)))
    c.send(str.encode(str(G)))
    Xa=int(input("Enter value for Xa:"))
    Ya=pow(G,Xa)%P
    print("Ya valuye is:",Ya)
    c.send(str.encode(str(Ya)))
    time.sleep(0.5)
    Yb=int(c.recv(1024).decode())
    Skey=pow(Yb,Xa)%P
    print("The Secret Key is:",Skey)
    c.send('Thank you for connecting'.encode())
    c.close()
    break