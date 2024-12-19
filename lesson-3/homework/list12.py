fruits = ['apple', 'banana', 'cherry', 'apple', 'pineapple', 'pear', 'peach', 'apple']

print('The original list is', fruits)

element = input('Enter an integer:\n')
index = int(input(f'Enter an index between 0 and {len(fruits)}:\n'))

fruits.insert(index, element)

print('The new list is', fruits)
