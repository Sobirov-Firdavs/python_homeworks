fruits = ['apple', 'banana', 'pear', 'apple', 'peach', 'pear', 'peach', 'apple']

print(f'The list is {fruits}.')

elements = ['apple', 'pear', 'peach']

print(f'The sublist is {elements}.')

check = 0

for element in elements:
    if element in fruits:
        check +=1
    else: check = check

if check == len(elements):
    print('The sublist is in the list.')
else: print('The sublist is not in the list.')