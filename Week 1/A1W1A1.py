input_string = input() 
year = int(input_string.split(":")[1]) 
months = year * 12
days = year * 365
print("Months:", months, ",", "Days:", days)