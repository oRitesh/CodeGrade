input_values = input("Please enter two numeric values: ").split()

A = int(input_values[0])
B = int(input_values[1])

print(f"You have entered that A = {A} and B = {B}")

A, B = B, A

print(f"Now A = {A} and B = {B}")