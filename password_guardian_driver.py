import pyperclip
from password_guardian_functions import *
from getpass import getpass



credential_list = []
app_loop = True
ui_loop = True
inner_loop = True
user_input = "" # ui input field
credential_name = "" # credential name field
credential_login = "" # credential login field
credential_password = "" #credential password field
app_password = "" # password guardian password field, allows user to access credentials throughout the app

quit_array = ['Q', 'q', 'Quit', 'quit'] # array of possible input for valid user input values for each option
find_array = ['F', 'f', 'Find', 'find']
add_array = ['A', 'a', 'Add', 'add']
delete_array = ['D', 'd', 'Delete', 'delete']
edit_array = ['E', 'e', 'Edit', 'edit']
view_array = ["V", "v", "View", "view"]
yes = ["Y", "y", "Yes", "yes", "YES"]
no = ["N", "n", "No", "no", "NO"]

while(app_loop):
    if(login_request()):

        print("Welcome to Password Guardian, you have sucessfully logged in!")
        string_list = decrypt_file() # obtain the decrypted login/passwords from data.txt
        credential_list = make_credentials(string_list) # convert decryted strings to credentials and populate list

        while(ui_loop):

            user_input = input('What would you like to do?\n'
                                'Enter from one of the options below:\n' 
                                'F, f, Find, find: to find a credential by application name\n'
                                'A, a, Add, add: to store a new credential\n'
                                'D, d, Delete, delete: to delete a credential\n'
                                'E, e, Edit, edit: to edit a credential\n'
                                'Q, q, Quit, quit:to quit\n')

            if(user_input in find_array):
                credential_name = input('What is the name of the application you would like your password for?\n')
                app_password = getpass()
            
                try:
                    credential_password, credential_login = find_credential(credential_name, credential_list, app_password)
                    pyperclip.copy(str(credential_password))
                    pyperclip.paste()
                    print("The password for " + credential_name + " is pasted to the clipboard!\n")
                    user_input = input("Would you like to view your login name?\n")
                    if(user_input in yes):
                        print(credential_login)
                except:
                    print("Either the password was incorrect or the credential does not exist."
                          "View your stored credential names with the (V)iew option.\n")
                
            elif(user_input in view_array):
                app_password = getpass()
                show_creds(credential_list, app_password)

            elif(user_input in quit_array):
                write_encrypted_file(credential_list)
                ui_loop = False
                app_loop = False

            elif(user_input in add_array):
                credential_name = input("Enter the name of the application you wish to generate a credential for: \n")
                credential_login = input("Enter the login name for the new credential:\n")
                credential_password = input("Enter the password for the new credential: \n")
                app_password = getpass()

                try:
                    new_credential = add_credential(credential_name, credential_login, credential_password, app_password, credential_list)
                    credential_list.append(new_credential)
                    for credential in credential_list:
                        print(credential.app_name)
                except:
                    print("Your password guardian password was incorrect, please try again using the correct password.\n")            

            elif(user_input in delete_array):
                credential_name = input("What is the name of the credential you want to delete?\n")
                app_password = getpass()

                try:
                    to_delete = find_credential_to_delete(credential_name, credential_list, app_password)
                    credential_list.remove(to_delete)
                except:
                    print("The credential entered does not exist or the password guardian password was incorrect."
                          "To view stored creddential names, please select the (V)iew option.")
            else: 
                print("Restarting UI loop.\n")
    else:
        print("Would you like to create a password guardian? Enter (y) for YES, (n) for NO")
        create_account()
        print("You may now log into password guardian!\n")


        

