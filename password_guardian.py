from cryptography.fernet import Fernet

# list vars to determine information
key_control = 0  # determine if need to generate a key or if a key is already stored


# Create the key unique to each user
key = Fernet.generate_key()





fp = open('data.txt', 'r')
list = []    # use heap or list?
for i in fp:
    list.append(i)
    print(list)
fp.close()
