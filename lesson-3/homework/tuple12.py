numbers = (1, 3, 5, 7, 6)

print(f'The tuple is {numbers}.')

numbers_list = list(numbers)

numbers_list.remove(max(numbers_list))

print(f'The second largest number in it is {max(numbers_list)}.')