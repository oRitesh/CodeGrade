input_string = input()
cost = float(input_string.split(":")[1])
tax = cost * 0.21
tip = cost * 0.15
total = cost + tax + tip
print(f"Tax: {tax:.3f}, Tip: {tip:.3f}, Total: {total:.3f}")