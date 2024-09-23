sides_input = input("Sides: ")

sides = sides_input.split(',')
a = int(sides[0].split('=')[1].strip())
b = int(sides[1].split('=')[1].strip())
c = int(sides[2].split('=')[1].strip())

if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")