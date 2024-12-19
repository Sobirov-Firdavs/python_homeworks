fruits = ('apple', 'banana', 'pear', 'apple', 'peach', 'pear', 'peach', 'apple')

print(f'The tuple is {fruits}.')

tuple_list = []

for fruit in fruits:
    if not fruit in tuple_list:
        tuple_list.append(fruit)
print(f'The new list is {tuple(tuple_list)}.')