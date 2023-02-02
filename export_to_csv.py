'''
    The `csv` library is a built-in library in Python for reading and writing CSV (Comma Separated Values) files
    It provides functions for reading and writing CSV files, allowing data to be easily stored and transferred between systems
    The library makes it easy to handle and manipulate tabular data in a programmatic way
'''

import csv
import os 

# def export_to_csv(db):
#     # Prompt user to choose what to export
#     while True:
#         action = input(
#             "Choose what to export:\n1.All data entered\n2.Total amount of orders per day "
#         )
        
#         # Export all data
#         if action == "1":
#             export_all_data(db)
#             return
        
#         # Export total amount of orders per day
#         elif action == "2":
#             export_total_per_day(db)
#             return
        
#         # Invalid input
#         else:
#             print("Please provide a valid input!\n")


# def export_all_data(db):
#     # Open the file 'all_data.csv' for writing
#     file_exists = os.path.exists('all_data.csv')
#     # Open the CSV file for writing `a` indicates appending file mode. Any data written will be added rather than overwriting
#     with open('all_data.csv', 'a' if file_exists else 'w') as f:
#         # Create a csv writer object
#         writer = csv.writer(f)
#         # Write the header row for the csv file
#         if not file_exists:
#             writer.writerow(['Customer name', 'customer_phone_number', 'Address', 'Date', 'Time', 'Total amount', 'User'])
#         # Loop through the `db` dictionary
#         for _user in db:
#             # Loop through the orders for each user
#             for order in db[_user]:
#                 # Write a row in the csv file for each order
#                 writer.writerow([order['customer_name'],order['customer_phone_number'], order['customer_address'], order['order_date'], order['order_time'], order['total_amount'],_user])


# def export_total_per_day(db):
#     # Check if the file 'totals_per_day.csv' exists
#     file_exists = os.path.exists('total_per_day.csv')
#     # Create an empty dictionary to store the total amount per day
#     totals_per_day_dict = {}
#     # Running total for all orders
#     total_amount = 0
    
#     #totals_per_day_str = ""
    
#     # Iterate through each user in the database
#     for _user in db:
#          # Iterate through each order for the user
#         for order in db[_user]:
#             if order["order_date"] in totals_per_day_dict:
#                 # If it is, add the total amount to the existing value
#                 totals_per_day_dict[order["order_date"]] += float(order["total_amount"])
#                  # If it isn't, add the date as a key and the total amount as the value
#             else:
#                 totals_per_day_dict[order["order_date"]] = float(order["total_amount"])
#             total_amount += float(order["total_amount"])
#     # Open the CSV file for writing `a` indicates appending file mode. Any data written will be added rather than overwriting
#     with open('total_per_day.csv', 'a' if file_exists else 'w') as f:
#         # Create a CSV writer object
#         writer = csv.writer(f)
#         # Write the header row
#         if not file_exists:
#             writer.writerow(['Date', 'Total amount'])
#         # Iterate through each day in the totals_per_day dictionary
#         for day in totals_per_day_dict:
#             # Write the data for each day
#             writer.writerow([day, totals_per_day_dict[day]])
#     print("Total amount:", total_amount)


def export_to_csv(db):
    while True:
        action = input(
            "Choose what to do:\n1. Open all_data.csv\n2. Total amount of orders per day "
        )
        
        # Open all_data.csv
        if action == "1":
            open_all_data()
            return
        
        # Export total amount of orders per day
        elif action == "2":
            open_total_amount()
            return
        
        # Invalid input
        else:
            print("Please provide a valid input!\n")

def open_all_data():
    try:
        with open('all_data.csv', 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("all_data.csv file not found.")
def open_total_amount():
    try:
        with open('total_per_day.csv', 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("total_per_day.csv file not found.")
        
total_calculated = False

def get_total_amount():
    global total_calculated
    if not total_calculated:
        calculate_total_amount()
        total_calculated = True
    return total_amount

def calculate_total_amount():
    global total_amount
    total_amount = 0
    for day in total_per_day:
        total_amount += day['amount']


def export_total_per_day(db):
    file_exists = os.path.exists('total_per_day.csv')
    totals_per_day_dict = {}
    total_amount = 0
    
    for _user in db:
        for order in db[_user]:
            if order["order_date"] in totals_per_day_dict:
                totals_per_day_dict[order["order_date"]] += float(order["total_amount"])
            else:
                totals_per_day_dict[order["order_date"]] = float(order["total_amount"])
            total_amount += float(order["total_amount"])
    
    with open('total_per_day.csv', 'a' if file_exists else 'w') as f:
    #with open('total_per_day.csv', 'w') as f:    
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Date', 'Total amount'])
        for day in totals_per_day_dict:
            writer.writerow([day, totals_per_day_dict[day]])
    print("Total amount:", total_amount)

def store_all_data(db):
    file_exists = os.path.exists('all_data.csv')
    with open('all_data.csv', 'a' if file_exists else 'w') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Customer name', 'customer_phone_number', 'Address', 'Date', 'Time', 'Total amount', 'User'])
        for _user in db:
            for order in db[_user]:
                writer.writerow([order['customer_name'],order['customer_phone_number'], order['customer_address'], order['order_date'], order['order_time'], order['total_amount'],_user])

def store_new_order(db, order):
    # Process and display the new order
    print("Processing order:", order)
    # Append the new order to the all_data.csv file
    with open("all_data.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(order)

# Call the store_new_order function whenever a new order is received
    while True:
        order = input("Enter a new order:")
        store_new_order(db, order)

def export_all_data(db):
    file_exists = os.path.exists('all_data.csv')
    with open('all_data.csv', 'a' if file_exists else 'w') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Customer name', 'customer_phone_number', 'Address', 'Date', 'Time', 'Total amount', 'User'])
        for _user in db:
            for order in db[_user]:
                writer.writerow([order['customer_name'], order['customer_phone_number'], order['customer_address'], order['order_date'], order['order_time'], order['total_amount'], _user])


def all_data_to_csv(db):
    export_all_data(db)
    export_total_per_day(db)
#    export_to_csv(db['total_amount'], "total_per_day.csv")

# def all_data_to_csv(db):
#     export_all_data(db)
#     export_total_per_day(db)