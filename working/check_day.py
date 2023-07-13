import datetime

# Define the starting day and the number of holidays
starting_day = input("Enter the starting day (MM/DD/YY): ")
number_of_holidays = int(input("Enter the number of holidays: "))

# Convert the starting day string to a datetime object
starting_day = datetime.datetime.strptime(starting_day, "%d/%m/%y").date()

# Calculate the current day
current_day = datetime.date.today()

# Calculate the number of days between the starting day and the current day
total_days = (current_day - starting_day).days

# Calculate the number of weekends in the range
weekend_days = sum(1 for i in range(total_days + 1) if (starting_day + datetime.timedelta(days=i)).weekday() >= 5)

# Calculate the adjusted number of days by subtracting weekends and holidays
adjusted_days = total_days - weekend_days - number_of_holidays

# Calculate the current day number by adding 1 to the adjusted days
current_day_number = adjusted_days + 1

# Print the current day number
print("Current day number:", current_day_number)

