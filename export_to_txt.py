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
    customer_names = set()
    
    # Read the existing customer names from the file
    with open("customer_names.txt", "r") as file:
        existing_names = file.read().splitlines()
        customer_names.update(existing_names)
        existing_phones = file.read().splitlines()
        customer_names.update(existing_phones)
    
    # Loop through the orders in the database
    for _user in db:
        for order in db[_user]:
            # Add the customer name to the set if it's not already there
            customer_names.add(order["customer_name"] + " " + order["customer_phone_number"])
            
    # Open a file to write the customer names to        
    with open('customer_names.txt', 'w') as f:
        # Write the customer names, separated by newline
        f.write("\n".join(customer_names))


def format_order(order):
    return f"{order['customer_name']:<21}|{order['customer_address']:<23}| {order['order_date']:<14} | {order['total_amount']:<13}"

from datetime import datetime

def export_orders_by_user(db, user):
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    orders = ""
    for _user in db:
        if _user == user:
            header = "Customer Name        Customer Address        Order Date       Total Amount\n"
            separator = "-" * len(header) + "\n"
            orders = separator + header + separator
            for order in db[user]:
                orders += format_order(order) + "\n"

    with open('orders.txt', 'a') as f:
        f.write("\n")  # Add empty line
        f.write(f"Report Date: {date_str}, Report Time: {time_str}, User of Report: {user}\n")
        f.write(orders)