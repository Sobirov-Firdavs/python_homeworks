numbers = {1, 4, 2, 7, 9, 33, 6}

print(f'The set is {numbers}.')

new = int(input('Enter an integer to remove from the set:\n'))

if new in numbers:
    numbers.remove(new)
    print(numbers)
else: print('The element is not existed in the set.')