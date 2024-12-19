fruits = ['apple', 'banana', 'pear', 'apple', 'peach', 'pear', 'peach', 'apple']

print(f'The list is {fruits}.')
element = input('Enter an element:\n')

indices = []

for fruit in fruits:
    if fruit == element:
        indices.append(fruits.index(fruit))
        fruits.insert(fruits.index(fruit), 'None')
        fruits.remove(fruit)
    else: indices = indices

print(f'All the indices of {element} in the list are {indices}.')