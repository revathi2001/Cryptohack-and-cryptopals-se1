from Crypto.Cipher import AES
import binascii
import codecs
import base64


key = 'YELLOW SUBMARINE'
msg=open('7.txt','r')
ciphertext = base64.b64decode(msg.read())
msg.close()
decipher = AES.new(key, AES.MODE_ECB)
print(decipher.decrypt(ciphertext))
