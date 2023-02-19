# Fernet module is imported from the 
# cryptography package
from cryptography.fernet import Fernet


def login_request():

    login_loop = True     # controls the login loop
    has_account = False   # returns if the user has an account

    while(login_loop):

        user_in = input('Do you have a login and password? Enter (y) for YES, Enter (n) for NO\n')

        if(user_in == 'y' or user_in == 'Y' or user_in == 'yes' or user_in == 'YES' or user_in == 'Yes'):
            with open('filekey.key', 'rb') as filekey:   # here we get the key to test the login/password only
                key = filekey.read()
                f = Fernet(key)
                login = input('Enter your username:\n').encode()          # encode is to make string behave with Fernet
                password = input('Enter your password:\n').encode()

                x = f.encrypt(login)                     # here we need to read in the first  encrypted credential object and match encrypted values
                y = f.encrypt(password)
                print(x)                                 # testing
                print(y)                                 # testing
                login_loop = False
                has_account = True
                # compare the password/login to the first credential object in data.txt, if match return true
        else:
            print("The user does not have an account. Please make an account.") 
            has_account = False
            login_loop = False

    return has_account

def create_account():                           # create account function, need to make sure a user cannot accidentally overwrite their account
                                                # if a new key is generated and written to filekey, everything is essentially lost
    create_loop = True

    while(create_loop):

        login = input("Enter a username for password guardian:\n").encode()  # encode is to make string behave with Fernet
        password = input("Enter your password for password:\n").encode()

        print("Are you happy with the following, ENTER (y) for YES or (n) for NO?\n")
        print(login.decode() + ' as login ' + password.decode() + ' as password')

        happy = input()
        
        if(happy == 'y' or happy == 'Y' or happy == 'YES' or happy == 'Yes'):
            create_loop = False

        else:
            print("Ok, try another login password combination.")

    key = Fernet.generate_key() # make the unique user key

    with open('filekey.key', 'wb') as filekey: # store the encrypted user key to the file
        filekey.write(key)

def get_key():                                      # returns the key to the user interface

    with open('filekey.key', 'rb') as filekey:
                key = filekey.read()
                f = Fernet(key)
    
    return f



  

