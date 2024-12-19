numbers = [1, 4, 2, 7, 9, 33, 6]

print(f'The list is {numbers}.')

even = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else: even = even
print(f'The even numbers in the list are {even}.')