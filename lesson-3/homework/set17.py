numbers = {1, 4, 2, 7, 9, 33, 6}

print(f'The set is {numbers}.')

odd = set()

for number in numbers:
    if number % 2 == 1:
        odd.add(number)

print(f'The odd numbers in the set are {odd}.')