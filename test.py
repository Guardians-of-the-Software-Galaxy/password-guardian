from cryptography.fernet import Fernet

print("Enter (y) to make key and print poop, Enter (n) to use key from file to print poop:\n")
x = input()
print(x)

if (x == 'y'):
    key = Fernet.generate_key() # make the unique user key1
    f = Fernet(key)
    x = f.encrypt('poop'.encode())
    print(x)
    y = f.decrypt(x)
    print(y)
    
    with open('testkey.key', 'wb') as testkey: # store the encrypted user key to the file
        testkey.write(key)

else:

     with open('testkey.key', 'rb') as testkey: # store the encrypted user key to the file
        key = testkey.read()

     f = Fernet(key)
     x = f.encrypt('poop'.encode())
     print(x)
     y = f.decrypt(x)
     print(y)
     
