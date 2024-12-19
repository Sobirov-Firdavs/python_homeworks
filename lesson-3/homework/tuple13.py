numbers = (1, 3, 5, 7, 6)

print(f'The tuple is {numbers}.')

numbers_list = list(numbers)

numbers_list.remove(min(numbers_list))

print(f'The second smallest number in it is {min(numbers_list)}.')