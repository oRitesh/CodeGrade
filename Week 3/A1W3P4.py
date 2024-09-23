def C_to_F(celcius):
    return (celcius * 9/5) + 32

print("°C\t°F")

for celcius in range(0, 101, 10):
    fahrenheit = C_to_F(celcius)

    print(f"{celcius}\t{fahrenheit}")