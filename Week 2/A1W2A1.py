# function is_input_valid(inp_date) to check required format
def is_input_valid(inp_date):
    if len(inp_date) != 10:
        return False
    
    # split the date and check for the required format
    parts = inp_date.split('-')
    
    if len(parts) != 3:
        return False
    
    year, month, day = parts
    
    # year is a 4 digit number
    if not (year.isdigit() and len(year) == 4):
        return False
    
    # month is a 2 digit number between 01 and 12
    if not (month.isdigit() and 1 <= int(month) <= 12):
        return False
    
    # day is a 2 digit number
    if not day.isdigit():
        return False
    
    # max days in a month = 31
    max_days = 31
    if int(month) in [4, 6, 9, 11]:  # all months with only 30 days
        max_days = 30
    elif int(month) == 2:  # february has 28 days
        max_days = 28
    
    # check if the given day isnt ourside of 1 and the max days
    if not (1 <= int(day) <= max_days):
        return False
    
    return True

# calculate the next date
def next_date(year, month, day):
    # days in every month
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # update the day
    day += 1

    # see if it goes to the next month
    if day > days_in_month[month - 1]:
        day = 1
        month += 1
    
    # see if it goes to the next year
    if month > 12:
        month = 1
        year += 1

    return year, month, day

# user input
inp_date = input("Input Date: ")

# validate input format
if not is_input_valid(inp_date):
    print("Input format ERROR. Correct Format: YYYY-MM-DD")
else:
    # extract year, month, and day from the input
    year, month, day = map(int, inp_date.split('-'))

    # calculate the next date
    new_year, new_month, new_day = next_date(year, month, day)

    # print nextdate
    print(f"Next Date: {new_year:04d}-{new_month:02d}-{new_day:02d}")
