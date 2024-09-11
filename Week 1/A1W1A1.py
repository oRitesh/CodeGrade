input_string = input()  # Asks user for input
year = int(input_string.split(":")[1]) # Seperates the input after the : then selects the number after :
months = year * 12 # Calculate months
days = year * 365 # Calculate days
print("Months:", months, ",", "Days:", days)