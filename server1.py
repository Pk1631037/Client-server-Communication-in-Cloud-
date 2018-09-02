import pyAesCrypt
from os import stat, remove
import socket
import time

s = socket.socket()         
print ("Socket successfully created")


port = 12338               


s.bind(('', port))        
print ("socket binded to %s" %(port))

s.listen(5)     

while True:

 c, addr = s.accept()     
 print ('Got connection from', addr)
 data1=c.recv(1024)
 byt1=data1.decode()
 print('File name is ',byt1)
 print('Encrypting.....')
 time.sleep(2)
 print('decrypting.....')
 time.sleep(2)

 bufferSize = 64 * 1024
 password = "foopassword"


 with open("data.txt", "rb") as fIn:
     with open("data.txt.aes", "wb") as fOut:
         pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)


 encFileSize = stat("data.txt.aes").st_size


 with open("data.txt.aes", "rb") as fIn:
     with open("dataout.txt", "wb") as fOut:
         try:
            
             pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
             
         except ValueError:
           
             remove("dataout.txt")
             print('Encryption and Decryption done1')
 print('After Encryption and decryption  the File is  send to Client  ')
 time.sleep(2)
 print('Encryption and Decryption done')
 print('Encrypted File is Stored in dataout.txt')
 file1 = open("dataout.txt","r+") 
 content=file1.readline()
 st=content
 byt=st.encode()
 c.send(byt)
 file1.seek(0)
 c.close()
 
