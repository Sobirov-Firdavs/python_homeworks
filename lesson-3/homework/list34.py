fruits = ['apple', 'banana', 'pear', 'cherry', 'melon', 'pineapple']

print(f'The list is {fruits}.')
factor = int(input('Enter a factor:\n'))

rotated_list = fruits[-factor:] + fruits[:-factor]

print(f'The rotated list is {rotated_list}.')