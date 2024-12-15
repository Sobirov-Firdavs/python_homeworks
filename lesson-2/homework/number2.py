a = float(input('You will enter three numbers. Enter the first:\n'))
b = float(input('Enter the second:\n'))
c = float(input('Enter the third:\n'))

largest = max(a, b, c)
smallest = min(a, b, c)

print(f'The largest number you have entered is {largest}')
print(f'The smallest number you have entered is {smallest}')