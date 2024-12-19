numbers = (-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6)
print(f'The tuple is {numbers}.')

numbers_list = list(numbers)

if numbers_list == sorted(numbers_list):
    print('The tuple is sorted.')
else: print('The tuple is not sorted.')