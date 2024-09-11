input_string = input() # Asks user for input
cost = float(input_string.split(":")[1]) # Splits user input after the : 
tax = cost * 0.21 # Calculate tax
tip = cost * 0.15 # Calculate tip
total = cost + tax + tip
print(f"Tax: {tax:.3f}, Tip: {tip:.3f}, Total: {total:.3f}") # Using an F string and giving fromatting to the numbers with .3f