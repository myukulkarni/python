
binary_numbers = input("Enter 4-digit binary numbers separated by commas: ").split(',')


divisible_by_5 = []


for binary in binary_numbers:
    
    decimal = int(binary, 2)
    
    if decimal % 5 == 0:
        divisible_by_5.append(binary)


print(",".join(divisible_by_5))
