
from password_guardian_functions import *


credential_list = []
ui_loop = True;
user_input = ""

if(login_request()):

    while(ui_loop):
        print("Welcome to Password Guardian, you have sucessfully logged in!")
        string_list = decrypt_file() # obtain the decrypted login/passwords from data.txt
        credential_list = make_credentials(string_list) # convert decryted strings to credentials and populate list

        user_input = input('What would you like to do?\n'
                            'Enter from one of the options below:\n' 
                            'F, f, Find, find: to find a credential by application name\n'
                            'A, a, Add, add: to store a new credential\n'
                            'D, d, Delete, delete: to delete a credential\n'
                            'E, e, Edit, edit: to edit a credential\n')
                        
        credential_list.append(add_credential('Gmail', 'poop@gmail.com', 'foobar1'))
        print([Credential.password for Credential in credential_list])
        print(find_crendential('Gmail', credential_list).password)
        pyperclip.copy(credential_list[0].password)
        pyperclip.paste

        # store the app credential first in the array or list to check passwords for content modification
        # call function to read encrypted data from data.txt into a list or array of credential objects 
        # access the array of credential objects based on application name
        # add or delete credential objects to array/list 
        # time out the user_interface loop
        # close the program option

else:
    print("Would you like to create a password guardian? Enter (y) for YES, (n) for NO")
    create_account()


        

