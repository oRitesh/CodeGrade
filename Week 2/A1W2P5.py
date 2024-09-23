date_input = input("Date: ")

month_day = date_input.split(',')
month = int(month_day[0].split(':')[1].strip())
day = int(month_day[1].split(':')[1].strip())

if month == 1 and day == 1:
    print("Nieuwjaarsdag")
elif month == 4 and day == 27:
    print("Koningsdag")
elif month == 5 and day == 5:
    print("Bevrijdingsdag")
elif month == 12 and day == 5:
    print("Sinterklaas")
elif month == 12 and day == 25:
    print("Kerstmis")
elif month == 12 and day == 26:
    print("Tweede kerstdag")
else:
    print("No holiday found on given input")