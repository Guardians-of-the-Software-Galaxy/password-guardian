import pyperclip
from password_guardian_functions import *


credential_list = []
ui_loop = True
inner_loop = True
user_input = "" # ui input field
credential_name = "" # credential name field
credential_password = "" #credential password field
app_password = "" # password guardian password field, allows user to access credentials throughout the app

quit_array = ['Q', 'q', 'Quit', 'quit'] # array of possible input for valid user input values for each option
find_array = ['F', 'f', 'Find', 'find']
add_array = ['A', 'a', 'Add', 'add']
delete_array = ['D', 'd', 'Delete', 'delete']
edit_array = ['E', 'e', 'Edit', 'edit']
view_array = ["V", "v", "View", "view"]

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
                            'E, e, Edit, edit: to edit a credential\n'
                            'Q, q, Quit, quit:to quit\n')

        if(user_input in find_array):
            credential_name = input('What is the name of the application you would like your password for?\n')
            app_password = input('Enter your password guardian password?\n')
            credential_password = find_credential(credential_name, credential_list, app_password)
            
            if(credential_password == "jeff_mcJeff_Jeff_McJefferson_Pearson"):
                print("Your application guardian password was incorrect, please try again with the correct password.\n")

            else:
                pyperclip.copy(str(credential_password))
                pyperclip.paste()
                print("The password for " + credential_name + " is pasted to the clipboard!\n") 

        elif(user_input in view_array):
            app_password = input("Enter your password guardian password:")
            show_creds(credential_list, app_password)

        elif(user_input in quit_array):
            ui_loop = False

        else: 
            print("Restarting UI loop.\n")
else:
    print("Would you like to create a password guardian? Enter (y) for YES, (n) for NO")
    create_account()


        

