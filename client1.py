import socket               

s = socket.socket()         

port = 12338        
 
s.connect(('192.168.56.1', port))
 
a=input('Enter The File Name TO Encrypt')
#st=a
#f=open("data.txt","wt")
byt=a.encode()
s.send(byt)
data2=s.recv(1024)
#data=s.recv(1024)
byt2=data2.decode()
print('After Encryption and decryption The Content in the file is    ')
print('"',byt2,'"')
#f.write(byt1)

s.close()       
