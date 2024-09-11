in_seconds = int(input("Enter the amount of seconds:"))

# Calculate hours, minutes, and remaining seconds
hours = in_seconds // 3600  # 1 hour = 3600 seconds
remaining_seconds = in_seconds % 3600 # Calculates the remaining second by using a % which devides and then gives the remains as an answer
minutes = remaining_seconds // 60  # 1 minute = 60 seconds
seconds = remaining_seconds % 60

# Output the result as whole numbers, .02d so that the seconds and minutes have a 0 in front when its a single number
print(f"{hours}:{minutes:02d}:{seconds:02d}")

# % is a float division, gives the remains of a division
# // is a floor division, gives the the result and discards the remains