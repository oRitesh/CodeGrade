number = input("Enter a 4 digit number:") # Asks user to input a 4 digit number

# Seperates numbers
d1 = int(number[0]) # Gets the first number from the number list
d2 = int(number[1]) # Gets the second number from the number list
d3 = int(number[2]) # Gets the third number from the number list
d4 = int(number[3]) # Gets the fourth number from the number list

total = d1 + d2 + d3 + d4 # Calculates the sum of all numbers

print(f"{d1}+{d2}+{d3}+{d4}={total}") # Prints out the numbers individually and shows the total
