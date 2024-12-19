fruits = ['apple', 'banana', 'pear', 'apple', 'peach', 'pear', 'peach', 'apple']

print(f'The list is {fruits}.')

new_list = []

for fruit in fruits:
    if not fruit in new_list:
        new_list.append(fruit)
print(f'The new list is {new_list}.')