'''
    The `csv` library is a built-in library in Python for reading and writing CSV (Comma Separated Values) files
    It provides functions for reading and writing CSV files, allowing data to be easily stored and transferred between systems
    The library makes it easy to handle and manipulate tabular data in a programmatic way
'''
import csv

def export_to_csv(db):
    # Prompt user to choose what to export
    while True:
        action = input(
            "Choose what to export:\n1.All data entered\n2.Total amount of orders per day "
        )
        
        # Export all data
        if action == "1":
            export_all_data(db)
            return
        
        # Export total amount of orders per day
        elif action == "2":
            export_total_per_day(db)
            return
        
        # Invalid input
        else:
            print("Please provide a valid input!\n")


def export_all_data(db):
    # Open the file 'all_data.csv' for writing
    with open('all_data.csv', 'w') as f:
        # Create a csv writer object
        writer = csv.writer(f)
        # Write the header row for the csv file
        writer.writerow(['Customer name', 'Address', 'Date', 'Total amount'])
        # Loop through the `db` dictionary
        for _user in db:
            # Loop through the orders for each user
            for order in db[_user]:
                # Write a row in the csv file for each order
                writer.writerow([order['customer_name'],order['customer_address'], order['order_date'], order['total_amount'], _user])


def export_total_per_day(db):
    # Create an empty dictionary to store the total amount per day
    totals_per_day_dict = {}
    
    totals_per_day_str = ""
    
    # Iterate through each user in the database
    for _user in db:
         # Check if the date is already in the dictionary
        for order in db[_user]:
            if order["order_date"] in totals_per_day_dict:
                # If it is, add the total amount to the existing value
                totals_per_day_dict[order["order_date"]] += float(order["total_amount"])
                 # If it isn't, add the date as a key and the total amount as the value
            else:
                totals_per_day_dict[order["order_date"]] = float(order["total_amount"])
    
    # Open the CSV file for writing
    with open('totals_per_day.csv', 'w') as f:
        # Create a CSV writer object
        writer = csv.writer(f)
        # Write the header row
        writer.writerow(['Date', 'Total amount'])
        # Iterate through each day in the totals_per_day dictionary
        for day in totals_per_day_dict:
            # Write the data for each day
            writer.writerow([day, totals_per_day_dict[day]])
