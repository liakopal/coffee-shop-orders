
'''
    This `login()` function prompts the user to enter their username and password.
    If the entered username and password are valid, the function returns the username.
    If the entered username and password are not valid, the function prompts the user to try again.
'''
import getpass
def login():
    # Prompt the user to enter their username with a while loop
    while True:
        username = input("Please provide username: ")
        # Prompt the user to enter their password
        password = getpass.getpass("Please provide password: ")
        # Check if the entered username and password are valid
        if check_user(username, password):
            # Return the username if the entered username and password are valid
            return username
        # Prompt the user to try again if the entered username and password are not valid
        print("Wrong Password, try again...\n")


def check_user(username, password):
    
    #Check if the provided username and password match the records in the accounts dictionary
    
    accounts = {"alex": "123", "marios": "456", "giota": "789"}
    if username in accounts and accounts[username] == password:
        return True
    return False

