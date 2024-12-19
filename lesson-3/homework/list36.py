numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]

print(f'The list is {numbers}.')

total = 0

for number in numbers:
    if number > 0:
        total += number
print(f'The sum of the positive numbers is {total}.')