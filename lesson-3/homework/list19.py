fruits = ['apple', 'banana', 'pear', 'apple', 'peach', 'pear', 'peach', 'apple']

print(f'The list is {fruits}.')

old_element = input('Enter any element in it:\n')

new_element = input('Enter a new element to replace the old one:\n')

index = fruits.index(old_element)
fruits.remove(old_element)
fruits.insert(index, new_element)

print(f'The new list is {fruits}.')