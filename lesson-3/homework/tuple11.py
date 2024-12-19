fruits = ('apple', 'banana', 'pear', 'apple', 'peach', 'pear', 'peach', 'apple')

fruits_list = list(fruits)

print(f'The tuple is {fruits}.')
element = input('Enter an element:\n')

indices = []

for fruit in fruits:
    if fruit == element:
        indices.append(fruits_list.index(fruit))
        fruits_list.insert(fruits_list.index(fruit), 'None')
        fruits_list.remove(fruit)
    else: indices = indices

print(f'All the indices of {element} in the tuple are {indices}.')