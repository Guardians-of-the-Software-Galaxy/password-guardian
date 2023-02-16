
# Fernet module is imported from the 
# cryptography package
from cryptography.fernet import Fernet
  
  
# key is generated
key = Fernet.generate_key()

with open('filekey.key', 'wb') as filekey:
   filekey.write(key)

# value of key is assigned to a variable
f = Fernet(key)
  
# the plaintext is converted to ciphertext
with open('data.txt', 'rb') as file:
    original = file.readline()
    print(original)
    token = f.encrypt(original)
    print(token)
    print('='*20)
    d_token = f.decrypt(token)
    print(d_token)
# display the ciphertext

  
# decrypting the ciphertext
#d = f.decrypt(token)
  
# display the plaintext and the decode() method 
# converts it from byte to string
#print(d.decode())