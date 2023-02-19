
from password_guardian_driver import *



if(login_request()):
    # read data.txt into a list
    print("Hello big butt!")
    # call function to read encrypted data from data.txt into a list or array of credential objects !LEAVE ENCRYPTED!

else:
    print("Would you like to create a password guardian? Enter (y) for YES, (n) for NO")
    create_account()

f = get_key()
message = f.encrypt(b'Hello big butt!')
print(message)
print(f.decrypt(message))
        

