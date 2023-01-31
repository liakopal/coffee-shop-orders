'''
    This function `export_to_txt` allows a user to export either the names of customers or orders entered
    by them in the database db to a .txt file
'''

def export_to_txt(db, user):
    
    # Take user input to choose what to export
    action = input(
        "Choose what to export:\n1.Names of customers \n2.Orders entered by user "
    )
    
    # Loop to validate user input
    while True:
        
        # If user chooses to export customer names
        if action == "1":
            export_customer_names(db)
            return
        
        # If user chooses to export orders entered by them
        elif action == "2":
            export_orders_by_user(db, user)
            return
        
        # If user input is invalid
        else:
            print("Please provide a valid input!\n")


def export_customer_names(db):
    
    # Create an empty set to store unique customer names
    customer = set()
    
    # Loop through the orders in the database
    for _user in db:
        for order in db[_user]:
            # Add the customer name to the set if it's not already there
            customer.add(order["customer_name"])
            
    # Open a file to write the customer names to        
    with open('customer_names.txt', 'w') as f:
        # Write the customer names, separated by newline
        f.write("\n".join(customer))


def export_orders_by_user(db, user):
    # Initialize an empty string to store the order information
    orders = ""
    
    # Loop through each user in the database
    for _user in db:
        # Check if the current user is the desired user
        if _user == user:
            # Loop through each order in the current user's order list
            for order in db[_user]:
                # Add the order information to the `order_info` string
                orders += f"{order['customer_name']}, {order['customer_address']}, {order['order_date']}, {order['total_amount']}\n"
    
    # Write the `order_info` string to a file named "orders.txt"
    with open('orders.txt', 'w') as f:
        f.write(orders)
