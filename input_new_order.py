
'''
    `uuid` is a Python library that provides universally unique identifiers (UUIDs) for objects
    It can be used to identify resources in a unique, unambiguous way 
'''

import uuid

'''
    The function `input_new_order(db, user)` adds a new order to the database
    `db` for a specific user `user`
'''
    
def input_new_order(db, user):
    
    # Prompt user for customer's name
    customer_name = input("Please provide customer's name:")
    
    # Prompt user for customer's address
    address = input("Please provide customer's address:")
    
    # Prompt user for date
    date = input("Please provide date:")
    
    # Prompt user for total amount
    total_amount = input("Please provide total amount:")
    
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

