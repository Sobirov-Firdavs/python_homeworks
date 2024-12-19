numbers = (1, 4, 2, 7, 9, 33, 6)

print(f'The tuple is {numbers}.')

element = int(input('Enter an element:\n'))

if element in numbers:
    print('The tuple contains that element')
else: print('The tuple does not contain that element.')