from datetime import date, datetime
# function to display information based on user input

def display_info(db):
    # loop until user provides valid input
    while True:
         # prompt user for input
        action = input(
            "Choose what to export:\n1.Numbers of order placed by one specific customer\n2.Number of orders in one specific day\n3.Total amount of all orders delivered\n4.Total amount of the orders placed by a specific customer\n5.Total amount of the orders placed by a specific day\n"
        )
        
        # if user inputs 1, display orders by customer from database
        if action == "1":
            customer = input("Type which customer's orders to display: ")
            print(display_orders_by_customer(db, customer))
            return
        
        # if user inputs 2, display orders in a day from database
        elif action == "2":
            day = input("Type which day to display (YYYY-MM-DD): ")
            print(count_orders_in_day(db, day))
            return
        
        # if user inputs 3, display total of all orders from database
        elif action == "3":
            print(count_total_of_all_orders(db))
            return
        
        # if user inputs 4, display total of specific customer from database
        elif action == "4":
            customer = input("Type which customer's total to display: ")
            print(count_total_of_specific_customer(db, customer))
            return
        
        # if user inputs 5, display total of specific day from database
        elif action == "5":
            day = input("Type which day to display (YYYY-MM-DD): ")
            print(count_total_amount_in_day(db, day))
            return
        
        # if user inputs invalid option, prompt for valid input
        else:
            print("Please provide a valid input!\n")


def count_orders_in_day(db, day):
    # Count the number of orders on a specific day.
    # This line initializes a variable count to zero.
    # This variable will be used to keep track of the number of orders placed on a given day
    count = 0
    
    # Starts a for loop that iterates through each customer in the db dictionary
    for _user in db:
        
        # Starts a nested for loop that iterates through each order of the current customer
        for order in db[_user]:
            
            # Checks if the current order's date is the same as the day argument passed to the function
            
            if day == order["order_date"]:
                
                
                # If the order's date matches the day argument, the count variable is incremented by 1
                count += 1
                
    # Checks if the count variable is still 0, indicating that no orders were found on the given day
    if count == 0:
        # If no orders were found on the given day, this line returns a string indicating that no orders were found
        return "No orders found on given day\n"
    
    
    # If at least one order was found on the given day,
    # this line returns a string indicating the number of orders found and the date
    return str(count) + " orders found on " + day
''' 
    The following function `display_orders_by_customer` takes two parameters, db and customer.
    db is the database which holds the orders data, customer is the name of the customer we want to retrieve the
    order information 
'''

def display_orders_by_customer(db, customer):
    # initialize a counter to track number of orders
    count = 0
    # loop through each customer in the database
    for _user in db:
        # Within the `for` loop, start another `for` loop that iterates over all the orders placed by the `_user`
        for order in db[_user]:
            # Check if the customer name in the current order is equal to the `customer` parameter passed to the function
            if customer == order["customer_name"]:
                # If the condition is met, increment the count by 1
                count += 1
    if count == 0:
        # Check if the `count` is equal to `0`. If the condition is met, return the string "No orders found for given customer\n"
        return "No orders found for given customer\n"
    # Return the orders variable
    return str(count) + " orders found for " + customer
''' 
    This function takes in a dictionary db as an argument and returns a string representation,
    of the total amount of all orders that were delivered.
'''
def count_total_of_all_orders(db):
    # Creates a variable named `total` and initializes it to 0.
    # This will be used to keep track of the total amount of all orders
    total = 0
    # Starts a for loop to iterate over all the customers in the `db` dictionary
    # The variable `_user` is used to represent each customer
    for _user in db:
        # Starts a nested for loop to iterate over all the orders for each customer
        # The variable order is used to represent each order for the current customer
        for order in db[_user]:
            # Adds the total amount of the current order to the `total` variable
            total += float(order["total_amount"])
    
    # Returns a string representation of the total amount of all orders delivered       
    # The string concatenates the following text and the value of `total` is converted to a string and `$` 
    return "Total amount of all orders delivered: " + str(total) + "$"


''' 
    The function count_total_of_specific_customer takes in a database db and a string customer
    It returns the total amount spent by the customer customer on all their orders.
'''

def count_total_of_specific_customer(db, customer):
    # Initializes a variable total to store the sum of all orders by the customer
    total = 0
    # Loops through each key in the database
    for _user in db:
        # Loops through each order in the value associated with the current key
        for order in db[_user]:
            # If the customer name in the current order matches the `customer` argument
            if customer == order["customer_name"]:
                # Increment the total by the value of `order["total_amount"]`
                total += float(order["total_amount"]) 
    
    # If the total is zero, it means no orders were found for the given customer
    if total == 0:
        return "No orders found for given customer.\n"
    

    #Return the total amount spent by the customer in the desired format
    #`customer` is a variable passed as an argument to the function, which holds the name of the specific customer
    #for whom the total amount of orders is calculated
    #`str(total)` is the total amount of the orders for the specific customer, which is a float value
    #and is converted to string using the str function
    #"$\n" is a string literal that indicates the currency used and adds a new line character at the end of the string
    #to separate it from other outputs
    
    return "Total amount for: " + customer + " is " + str(total) + "$\n"

'''
    The function count_total_amount_in_day takes in a database db and a string day as inputs
    The function uses nested for loops to iterate over the data in the database
    and to calculate the total amount of orders placed on the given day
'''
def count_total_amount_in_day(db, day):
    # Starts by initializing a variable `total` to 0, which will be used to store the total amount of the orders
    total = 0
    # The first for loop iterates over each key in `db` 
    for _user in db:
        # The second for loop iterates over the list of orders for each customer stored under the respective key
        for order in db[_user]:
            # For each order, the function checks if the date of the order matches the given day
            if day == order["order_date"]:
                # If the date matches, the function adds the total_amount of the order to the total variable
                total += float(order["total_amount"])
    if total == 0:
        # If the total is still 0, it means that there were no orders found on the given day, and the function returns the string
        return "No orders found on given day\n"
    # Otherwise, the function returns the total amount of orders placed
    # The "+" symbol in this case, it is combining the string representation of the "total" variable (converted to a string using the str() function)
    # The string "$ orders found on ", and the "day" variable into a single string, which is then returned by the function
    return str(total) + "$ orders found on " + day
