position = input("Position: ")

column_letter = position[0]
row_number = int(position[1])

column_number = ord(column_letter) - ord('A') + 1

if (column_number + row_number) % 2 == 0:
    print("Black")
else:
    print("White")