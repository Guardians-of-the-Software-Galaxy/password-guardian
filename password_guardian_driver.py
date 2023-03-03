
from password_guardian_functions import *

credential_list = []

if(login_request()):
    print("Welcome to Password Guardian, you have sucessfully logged in!")
    string_list = decrypt_file()
    print ([line for line in string_list])
    credential_list = make_credentials(string_list)
    credential_list.append(add_credential('Gmail', 'poop@gmail.com', 'foobar1'))
    print([Credential.password for Credential in credential_list])
    print(find_crendential('Gmail', credential_list).password)
    # store the app credential first in the array or list to check passwords for content modification
    # call function to read encrypted data from data.txt into a list or array of credential objects 
    # access the array of credential objects based on application name
    # add or delete credential objects to array/list 
    # time out the user_interface loop
    # close the program option

else:
    print("Would you like to create a password guardian? Enter (y) for YES, (n) for NO")
    create_account()


        

