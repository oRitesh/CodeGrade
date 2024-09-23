human_years = float(input("Human years: "))

if human_years < 0:
    print("Only positive numbers are allowed")
else:
    if human_years <= 2:
        dog_years = human_years * 10.5
    else:
        dog_years = (2 * 10.5) + (human_years - 2) * 4
    

print(f"Dog years: {dog_years}")