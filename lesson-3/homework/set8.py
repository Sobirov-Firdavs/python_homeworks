numbers = {1, 4, 2, 9, 33, 6}

print(f'The set is {numbers}.')

element = int(input('Enter an element:\n'))

if element in numbers:
    numbers.remove(element)
    print(f'The new set is {numbers}.')
else: print('The set does not contain thsi element.')