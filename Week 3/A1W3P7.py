truth_values = [(True, True), (True, False), (False, True), (False, False)]

def print_and_truth_table():
    print("AND Truth Table")
    for a, b in truth_values:
        result = a and b
        print(f"{a} + {b} = {result}")
    print()  

def print_or_truth_table():
    print("OR Truth Table")
    for a, b in truth_values:
        result = a or b
        print(f"{a} + {b} = {result}")
    print()  

print_and_truth_table()
print_or_truth_table()