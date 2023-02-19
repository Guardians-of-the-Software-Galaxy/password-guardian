# Fernet module is imported from the 
# cryptography package
from cryptography.fernet import Fernet


def login_request():

    login_loop = True
    x = True

    while(login_loop):

        user_in = input('Do you have a login and password? Enter (y) for YES, Enter (n) for NO\n')

        if(user_in == 'y' or user_in == 'Y' or user_in == 'yes' or user_in == 'YES' or user_in == 'Yes'):
            with open('filekey.key', 'rb') as filekey:
                key = filekey.read()
                f = Fernet(key)
                login = input('Enter your username:\n').encode()
                password = input('Enter your password:\n').encode()

                x = f.encrypt(login)
                y = f.encrypt(password)
                print(x)
                print(y)
                login_loop = False
        else:
            print("The user does not have an account. Please make an account.")
            x = False
            login_loop = False

    return x