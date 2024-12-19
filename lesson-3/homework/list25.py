from copy import deepcopy

numbers = [1, 4, 2, 7, 9, 33, 6]

numbers1 = deepcopy(numbers)

print(f'The former list is {numbers}.')
print(f'The copy of it is {numbers1}.')