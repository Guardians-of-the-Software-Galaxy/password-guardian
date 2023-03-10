# Fernet module is imported from the 
# cryptography package
from cryptography.fernet import Fernet

# Below is the credential object/class

################################################################

class Credential:
    
    def __init__(self, name, login, password):
        self.app_name = name
        self.login = login
        self.password = password

################################################################

# Below is the login function.
# 1) Obtain the login and password from the user
# 2) Read and decrypt the application credentials from database file
# 3) Compare the credentials and return true if login was successful

################################################################

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
                password = input('Enter your password:\n').encode()       # encode as binary string
               
            with open('data.txt', 'r') as data:
                app_check = f.decrypt(data.readline().strip('\n').encode()) # encode as binary because the file was stored as text
                log_check = f.decrypt(data.readline().strip('\n').encode()) 
                pass_check = f.decrypt(data.readline().strip('\n').encode())     
                login_loop = False
                if ((login == log_check) and (password == pass_check)): # verify credentials
                    print("Login successful!")
                    has_account = True
                # compare the password/login to the first credential object in data.txt, if match return true
        else:
            print("The user does not have an account. Please make an account.") 
            login_loop = False
            return False

    return has_account, login

################################################################


# Below is the function that creates a user account. 
# 1) Creates a key and stores it for subsequent use
# 2) Create username and password for the application
# 3) Encrypt and store the information in the database file

################################################################

def create_account():                           # create account function, need to make sure a user cannot accidentally overwrite their account
                                                # if a new key is generated and written to filekey, everything is essentially lost
    create_loop = True

    while(create_loop):

        login = input("Enter a username for password guardian:\n").encode()  # encode is to make string behave with Fernet
        password = input("Enter your password for password:\n").encode()     # encode as binary string

        print("Are you happy with the following, ENTER (y) for YES or (n) for NO?\n") # display credentials and verify happiness
        print(login.decode() + ' as login ' + password.decode() + ' as password')

        happy = input()
        
        if(happy == 'y' or happy == 'Y' or happy == 'YES' or happy == 'Yes'): #done
            create_loop = False

        else:
            print("Ok, try another login password combination.") # try again

    key = Fernet.generate_key() # make the unique user key

    with open('filekey.key', 'wb') as filekey: # store the encrypted user key to the file
        filekey.write(key)

    f = Fernet(key) # creates the key object
    login = f.encrypt(login) # encrypt the usful info
    password = f.encrypt(password)
    app_name = f.encrypt("password_guardian".encode())
    with open('data.txt', 'w') as data:
        data.write(app_name.decode() + '\n') # decode from binary to text for storage
        data.write(login.decode() + '\n') # write the credential info to be checked for further use
        data.write(password.decode() + '\n')

################################################################

# Below is the get key function
# Simply returns the key to the user interface

################################################################
def get_key():                                      # returns the key to the user interface

    with open('filekey.key', 'rb') as filekey:
                key = filekey.read()
                f = Fernet(key)
    
    return f

################################################################




################################################################

# Below is the function to read the lines from data.txt, decrypt,
# and place them into the credential.

################################################################

def decrypt_file():

    lines = []
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
        f = Fernet(key)
   
    with open('data.txt', 'r') as data:
        cred_list = []
        for line in data:
            lines.append(f.decrypt(line.strip('\n').encode()).decode())

    return lines

################################################################

################################################################

# Below is the function to add a new credential to the list.

################################################################

def add_credential(app_name, login, password):
    new_credential = Credential(app_name, login, password)

    return new_credential


################################################################

# Below is the function to make credentials from file.

################################################################

def make_credentials(string_list):

    crendential_list = []
    for i in range(0,len(string_list), 3):
        app_name = string_list[i]
        login = string_list[i + 1]
        password = string_list[i + 2]
        crendential_list.append(Credential(app_name, login, password))

    
    return crendential_list

################################################################

# Below is the function to make credentials from file.

################################################################

def find_crendential(credential_name, credential_list):
    for credential in credential_list:
        if(credential.app_name is credential_name):
            return credential

    return "No cred found."

