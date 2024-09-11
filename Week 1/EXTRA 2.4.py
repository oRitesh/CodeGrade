input_values1 = input("Enter the base and height of the first triangle: ").split()
input_values2 = input("Enter the base and height of the second triangle: ").split()

base_1 = float(input_values1[0])
height_1 = float(input_values1[1])

base_2 = float(input_values2[0])
height_2 = float(input_values2[1])

print("The sum of the 2 areas = ", (((0.5 * height_1 * base_1) + (0.5 * height_2 * base_2))))

