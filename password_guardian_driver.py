from password_guardian_functions import *
from getpass import getpass
import pyperclip


credential_list = []
app_loop = True
ui_loop = True
inner_loop = True
user_input = ""  # ui input field
credential_name = ""  # credential name field
credential_login = ""  # credential login field
credential_password = ""  # credential password field
# password guardian password field, allows user to access credentials throughout the app
app_password = ""

# array of possible input for valid user input values for each option
quit_array = ['Q', 'q', 'Quit', 'quit']
find_array = ['F', 'f', 'Find', 'find']
add_array = ['A', 'a', 'Add', 'add']
delete_array = ['D', 'd', 'Delete', 'delete']
edit_array = ['E', 'e', 'Edit', 'edit']
view_array = ["V", "v", "View", "view"]
yes = ["Y", "y", "Yes", "yes", "YES"]
no = ["N", "n", "No", "no", "NO"]

print("Disclaimer: This application stores application name, login name, and password for applications you would like to track."
      " The application stores all information in the database file as encrypted data using the Fernet encryption package."
      " To support heightened security, the application has no forgot password feature, in the case of a forgotten password, you must"
      " reset your entire program and start over. Password guardian stores all information locally meaning that associated files are encrypted"
      " at rest. This program generates two additional files, one to store the encrypted key, and one to store encrypted credential information."
      "If you accidentally say that you do not have a password guardian account when one exists, simply close the program with ctrl + c before"
      " creating new login for this application. PLEASE RUN ===> pip3 install pytimedinput <=== Enjoy! <('.'<)<('.')>(>'.')>")
print("\n")

while (app_loop):
    if (login_request()):

        print("Welcome to Password Guardian, you have sucessfully logged in!")
        string_list = decrypt_file()  # obtain the decrypted login/passwords from data.txt
        # convert decryted strings to credentials and populate list
        credential_list = make_credentials(string_list)

        while (ui_loop):

            user_input = get_ui_input()
            print(user_input)

            if (user_input == ""):
                app_loop = False
                ui_loop = False
                write_encrypted_file(credential_list)
                credential_list = []
                string_list = []
                user_input = ""  # clean up
                credential_name = ""  # clean up
                credential_login = ""  # cleanup
                credential_password = ""  # cleanup
                app_password = ""  # cleanup
                # make sure nothing can be pasted accidentally or by someone else
                pyperclip.copy("<('.'<)<('.')>(>'.')>")
                pyperclip.paste()
                ui_loop = False
                app_loop = False

            elif (user_input in find_array):
                credential_name = input(
                    "What is the name of the credential you wish to use?\n")
                app_password = getpass()

                try:
                    credential_password, credential_login = find_credential(credential_name, credential_list, app_password)
                    pyperclip.copy(str(credential_password))
                    pyperclip.paste()
                    print("The password for " + credential_name +
                          " is pasted to the clipboard!\n")
                    user_input = input(
                        "Would you like to view your login name?\n")
                    if (user_input in yes):
                        print(credential_login)
                except:
                    print("Either the password was incorrect or the credential does not exist. View your stored credential names with the (V)iew option.\n")

            elif (user_input in view_array):
                app_password = getpass()
                show_creds(credential_list, app_password)

            elif (user_input in quit_array):
                write_encrypted_file(credential_list)
                credential_list = []
                string_list = []
                user_input = ""  # clean up
                credential_name = ""  # clean up
                credential_login = ""  # cleanup
                credential_password = ""  # cleanup
                app_password = ""  # cleanup
                # make sure nothing can be pasted accidentally or by someone else
                pyperclip.copy("<('.'<)<('.')>(>'.')>")
                pyperclip.paste()
                ui_loop = False
                app_loop = False

            elif (user_input in edit_array):
                credential_name = input(
                    "What is the name of the credential you wish to use?\n")
                app_password = getpass(
                    "Enter your password guardian password: \n")
                edit_cred(credential_name, app_password, credential_list)

            elif (user_input in add_array):
                credential_name = input(
                    "What is the name of the credential you wish to use?\n")
                credential_login = input(
                    "What is the login name you wish to store for this credential?\n")
                credential_password = getpass(
                    "Enter the password for the new credential: \n")
                app_password = getpass(
                    "Enter your password guardian password: \n")
                add_credential(credential_name, credential_login, credential_password, app_password, credential_list)

            elif (user_input in delete_array):
                credential_name = input(
                    "What is the name of the credential you want to delete?\n")
                app_password = getpass()
                delete_credential(credential_name, credential_list, app_password)
                
            else:
                print("Restarting UI loop.\n")
    else:
        user_input = input(
            "Would you like to create a password guardian? Enter (y) for YES, (n) for NO")
        if (user_input in yes):
            create_account()
            print("You may now log into password guardian!\n")
        else:
            print(
                "Thanks for checking us out, consider using this application in the future.\n")
            app_loop = False
