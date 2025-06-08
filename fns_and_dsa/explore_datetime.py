from datetime import datetime, timedelta
# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now() # Get current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S") # Format it
    print("Current Date and Time:", formatted_date) 

# Part 2: Calculate a Future Date
 def calculate_future_date():
     try:
         number_of_days = int(input("Enter the number of days to add: "))
         future_date = datetime.now() + timedelta(days=number_of_days)
         print("Future Date (YYYY-MM-DD):", future_date.strftime("%Y-%m-%d"))
         except ValueError: print("Invalid input! Please enter an integer number of days.") 

# Run the functions
display_current_datetime()
calculate_future_date()
