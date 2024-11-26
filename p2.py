
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))


for i in range(len(numbers)):
    if numbers[i] > 10:
        numbers[i] = '*'

print(numbers)
