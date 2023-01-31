
'''
    `uuid` is a Python library that provides universally unique identifiers (UUIDs) for objects
    It can be used to identify resources in a unique, unambiguous way 
'''

import uuid
from datetime import datetime
def input_new_order(db, user):
    
    while True:
        # Prompt user for customer's name
        customer_name = input("Please provide customer's name:")
        
        if not customer_name.isalpha():
            print("Error: Customer name is required.")
            continue
        else:
            break
    while True:
        # Prompt user for customer's address
        address = input("Please provide customer's address:")
        
        if not address.isalpha():
            print("Error: Address is required.")
            continue
        else:
            break
     # Prompt user for date
    while True:
        date = input("Please provide date:")
        try:
            order_date = datetime.strptime((date), '%d/%m/%Y')
            break
        except ValueError:
                
            print("Error: Date is required.")
            continue

    # Prompt user for total amount
    while True:
        total_amount = input("Please provide total amount:")
        try:
            total_amount = float(total_amount)
            break
        except ValueError:
            print("Error: Total amount is required and must be a number.")
        # Append the order information to the database
    db[user].append(
        {
            "customer_name": customer_name,
            "customer_address": address,
            "order_date": date,
            "total_amount": total_amount,
            "user": user,
            "customer_id": uuid.uuid1()
            # a unique customer ID generated using uuid.uuid1()
        
        })
    
    # Return the updated database
    return db

