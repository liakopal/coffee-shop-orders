
'''
    `uuid` is a Python library that provides universally unique identifiers (UUIDs) for objects
    It can be used to identify resources in a unique, unambiguous way 
'''
#from export_to_csv import all_data_to_csv

from datetime import date, datetime

import uuid


from datetime import datetime, time


'''
    The function `input_new_order(db, user)` adds a new order to the database
    `db` for a specific user `user`
'''


def input_new_order(db, user):
    
    while True:
        # Prompt user for customer's name
        #customer_name = input("Please provide customer's name:")
        first_name = input("Please provide customer's first name:")
        last_name = input("Please provide customer's last name:")
        
        if not first_name.isalpha() or not last_name.isalpha():
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
        
    date = str(datetime.now().date())
    time = str(datetime.now().time())[:8]
    
    while True:
        # Prompt user for customer's mobile number
        phone_number = input("Please provide customer's mobile number:")
        
        if not phone_number.isdigit() or len(phone_number) != 10:
            print("Error: Mobile number is required and must be 10 digits.")
            continue
        else:
            break  
  
    while True:
        total_amount = input("Please provide total amount:")
        try:
            total_amount = float(total_amount)
            break
        except ValueError:
            print("Error: Total amount is required and must be a number.")
        
    # Concatenate the first and last name
    customer_name = first_name + " " + last_name    
    # Append the order information to the database
    db[user].append(
        {
            "customer_name": customer_name,
            "customer_address": address,
            "customer_phone_number": phone_number,
            "order_date": date,
            "order_time": time,
            "total_amount": total_amount,
            "user": user,
            "customer_id": uuid.uuid1()
            # a unique customer ID generated using uuid.uuid1()
        
        })
    
    # Call the export_to_csv function to export the database to a csv file
    from export_to_csv import all_data_to_csv 
    all_data_to_csv(db)    
    # Return the updated database
    
    return db
