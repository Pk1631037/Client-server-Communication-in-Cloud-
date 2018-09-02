import pyAesCrypt
from os import stat, remove
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "foopassword"

# encrypt
with open("data.txt", "rb") as fIn:
    with open("data.txt.aes", "wb") as fOut:
        pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)

# get encrypted file size
encFileSize = stat("data.txt.aes").st_size

# decrypt
with open("data.txt.aes", "rb") as fIn:
    with open("dataout.txt", "wb") as fOut:
        try:
            # decrypt file stream
            pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
            print('Encryption and Decryption done')
        except ValueError:
            # remove output file on error
            remove("dataout.txt")
            print('Encryption and Decryption done1')
