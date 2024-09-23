binary_number = input("Binary: ")  

binary_number = binary_number[::-1]  
decimal_number = 0  

for i in range(len(binary_number)):  
  
    digit = int(binary_number[i])  
    power = 2 ** i  
    result = digit * power  
   
    decimal_number += result  
print(decimal_number)    