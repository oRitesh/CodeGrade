def multiply_table():
    print("   ", end="")
    for i in range(1, 11):
        print(f"{i:3}", end="")  # label columms 1-10
    print()  # new line

    # print multiplication
    for i in range(1, 11):
        print(f"{i:2} ", end="")  # label rows 1-10
        for j in range(1, 11):
            print(f"{i * j:3}", end="")  # product of row and columm
        print()  # new line

multiply_table()