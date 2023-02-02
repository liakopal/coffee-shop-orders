
'''
    This code implements a simple program that keeps track of orders made by customers
'''
from login import login
from input_new_order import input_new_order
from export_to_txt import export_to_txt
from export_to_csv import export_to_csv
from display_info import display_info

''' 
    The main() function serves as the starting point of the program
'''

def main():
    # `user = login()` - calls the `login()` function, which is not defined in the code, and assigns the returned value to the `user` variable
    user = login()
    # Prints a welcome message to the user by inserting the value of the `user` variable in the message using the f-string
    print(f"Welcome {user}!")
    # Creates an empty dictionary `db`
    db = {}
    # Creates an empty list as the value of the key `user` in the dictionary `db`
    db[user] = []
    # Creates an infinite loop
    while True:
        # Takes an input from the user with a message to select an action
        action = input(
            "Please select action:\n1.Input order\n2.Export orders to txt\n3.Export all data to csv\n4.Display more info\n"
        )
        # Checks if the value of action is equal to 1, if it is, the program executes the code block under it
        if action == "1":
            # Calls the input_new_order(db, user) function, which is not defined in the code, with arguments `db` and `user`
            # It assigns the returned value to the `db` variable
            db = input_new_order(db, user)
            # Code to add order to the `db` dictionary
        # Checks if the value of `action` is equal to 2, if it is, the program executes the code block under it
        elif action == "2":
            # Calls the `export_to_txt(db, user)` function, with arguments `db` and `user`
            export_to_txt(db, user)
        # Checks if the value of `action` is equal to 3
        elif action == "3":
            # calls the `export_to_csv(db)` function, with the argument `db`
            export_to_csv(db)
        # Checks if the value of `action` is equal to 4
        elif action == "4":
            # Calls the `display_info(db)` function, with the argument `db`
            display_info(db)
        # If the value of action is not equal to any of the above values, the program executes the code block under it
        else:
            #  prints a message to provide a valid input
            print("Please provide a valid input!\n")

# Calls the `main()` function to start the program
main()
