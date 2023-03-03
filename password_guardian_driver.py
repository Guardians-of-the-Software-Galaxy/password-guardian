
from password_guardian_functions import *

credential_list = []

if(login_request()):
    print("Welcome to Password Guardian, you have sucessfully logged in!")
    crendential_list = decrypt_file()
    # store the app credential first in the array or list to check passwords for content modification
    # call function to read encrypted data from data.txt into a list or array of credential objects 
    # access the array of credential objects based on application name
    # add or delete credential objects to array/list 
    # time out the user_interface loop
    # close the program option

else:
    print("Would you like to create a password guardian? Enter (y) for YES, (n) for NO")
    create_account()


        

