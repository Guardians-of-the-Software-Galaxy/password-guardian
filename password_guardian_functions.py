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

def login_request(credential_list, app_password):

    if(app_password == credential_list[0].password):  
        return True

    return False
    
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

def add_credential(app_name, login, password, guardian_password, credential_list):
    if(guardian_password == credential_list[0].password):
        new_credential = Credential(app_name, login, password)
    else:
        return
    return new_credential


################################################################

################################################################

# Below is the function to delete a credential to the list.

################################################################

def find_credential_to_delete(credential_name, credential_list, app_password):
    if(app_password == credential_list[0].password):
        for credential in credential_list:
            if(credential.app_name == credential_name):
                return credential
    else:
        return


################################################################

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

def find_credential(credential_name, credential_list, password):
    if(password == credential_list[0].password):
        for credential in credential_list:
            if(credential.app_name == credential_name):
                print(credential.password + "\n")
                return credential.password
    else:
        return

################################################################

# Below is the function to display the list of credential names

################################################################

def show_creds(credential_list, password):
    if(password == credential_list[0].password):
        for credential in credential_list:
            print(credential.app_name)

    else:
        print("Please enter the correct password guardian password to view the list of applications\n")

################################################################

################################################################

# Below is the function to display the list of credential names

################################################################

def write_encrypted_file(credential_list):
    f = get_key()
    with open('data.txt', 'w') as data:
        for credential in credential_list:
            app_name = f.encrypt(credential.app_name.encode())
            login = f.encrypt(credential.login.encode())
            pass_word = f.encrypt(credential.password.encode())
            data.write(app_name.decode() + '\n') # decode from binary to text for storage   
            data.write(login.decode() + '\n')     
            data.write(pass_word.decode() + '\n')



################################################################

