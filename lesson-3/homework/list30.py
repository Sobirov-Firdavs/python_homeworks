from copy import deepcopy

numbers1 = [1, 4, 2, 9, 33, 6]

print(f'The list is {numbers1}.')

numbers2 = deepcopy(numbers1)

numbers1.sort()

if numbers1 == numbers2:
    print('The list is sorted.')
else: print('The list is not sorted.')