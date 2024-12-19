numbers = [1, 4, 2, 7, 9, 33, 6]

print(f'The list is {numbers}.')

odd = []

for number in numbers:
    if number % 2 == 1:
        odd.append(number)
    else: odd = odd
print(f'The even numbers in the list are {odd}.')