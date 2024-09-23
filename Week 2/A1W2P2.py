number = int(input("Year: "))

if number % 400 == 0:
    print("Leap year")
elif number % 100 == 0:
    print("Not a leap year")
elif number % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")