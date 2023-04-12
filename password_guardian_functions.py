# Fernet module is imported from the 
# cryptography package
from cryptography.fernet import Fernet
from getpass import getpass
from pytimedinput import timedInput
from getpass import getpass

quit_array = ['Q', 'q', 'Quit', 'quit'] # array of possible input for valid user input values for each option
find_array = ['F', 'f', 'Find', 'find']
add_array = ['A', 'a', 'Add', 'add']
delete_array = ['D', 'd', 'Delete', 'delete']
edit_array = ['E', 'e', 'Edit', 'edit']
view_array = ["V", "v", "View", "view"]
yes = ["Y", "y", "Yes", "yes", "YES"]
no = ["N", "n", "No", "no", "NO"]

################################################################

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
                password = getpass().encode()      # encode as binary string
               
            with open('data.txt', 'r') as data:
                app_check = f.decrypt(data.readline().strip('\n').encode()) # encode as binary because the file was stored as text
                log_check = f.decrypt(data.readline().strip('\n').encode()) 
                pass_check = f.decrypt(data.readline().strip('\n').encode())     
                
                if ((login == log_check) and (password == pass_check)): # verify credentials
                    print("Login successful!")
                    has_account = True
                    login_loop = False
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
        
        if(happy == 'y' or happy == 'Y' or happy == 'YES' or happy == 'Yes' or happy== 'yes'): #done
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
        for credential in credential_list:
            if credential.app_name == app_name:
                print("The credential with that name already exists, please check yourself or delete the existing credential with that name using (V)iew.\n")
                return credential_list
        new_credential = Credential(app_name, login, password)
        credential_list.append(new_credential)
    return
################################################################

################################################################

# Below is the function to delete a credential to the list.

################################################################

def delete_credential(credential_name, credential_list, app_password):
    d_cred = False
    if(app_password == credential_list[0].password):
        if(credential_name == "password_guardian"):
            print("You cannot delete your password guardian credential. If you no longer wish to use password guardian,"
                  " delete data.txt and fliekey.key from the program directory.\n")
        for credential in credential_list:
            if(credential.app_name == credential_name and credential.app_name != "password_guardian"):
                print("Deleting " + credential.app_name + "\n")
                credential_list.remove(credential)
                d_cred = True
    if not d_cred:
        print("The credential " + credential_name + " is not stored in password guardian.\n")
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
                return credential.password, credential.login
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

def get_ui_input():
    user_input, timed_out = timedInput('What would you like to do?\n'
                                       'Enter from one of the options below:\n' 
                                       'F, f, Find, find: to find a credential by application name\n'
                                       'A, a, Add, add: to store a new credential\n'
                                       'D, d, Delete, delete: to delete a credential\n'
                                       'E, e, Edit, edit: to edit a credential\n'
                                       'V, v, View, view: to view credential list\n'
                                       'Q, q, Quit, quit:to quit\n', timeout = 30)
    if(timed_out):
        print("Timed out when waiting for input.")
        print(f"User-input so far: '{user_input}'")

    return user_input
################################################################

# Below is the function to display the list of credential names

################################################################

def edit_cred(credential_name, app_password, credential_list):
    new_name = ""
    new_login = ""
    new_pass = ""
    user_input = ""
    change_name = False
    change_login = False
    change_pass = False
 
    if(app_password == credential_list[0].password):
        
        user_input = input("Would you like to change the credential name? (y/n): ")
        if(user_input in yes):
            change_name = True
            new_name = input("What would you like the name of the credential to be? ")
    
        user_input = input("Would you like to change the login name for this credential? (y/n): ")
        if(user_input in yes):
            change_login = True
            new_login = input("What would you like the login name to be? ")

        user_input = input("Would you like to change the password for the credential? (y/n): ")
        if user_input in yes:
            change_pass = True
            new_pass = getpass("What would you like the password of the credential to be? ")

        user_input = input("Are you happy with " + new_name + " and " + new_login + " for this credential?")

        for credential in credential_list:  
            if(credential_name == credential.app_name and credential_name != "password_guardian" and change_name):
                credential.app_name = new_name
                print("hello app name\n")
                # codiga-disable
                if(change_login):
                    credential.login = new_login
                    print("hello login\n")
                    # codiga-disable
                    if(change_pass):
                        print("hello \n")
                        credential.password = new_pass

################################################################