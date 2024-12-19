numbers = {1, 4, 2, 7, 9, 33, 6}

print(f'The set is {numbers}.')

new = int(input('Enter an integer to add to the set:\n'))

if not new in numbers:
    numbers.add(new)
    print(numbers)
else: print('The element is already existed in the set.')