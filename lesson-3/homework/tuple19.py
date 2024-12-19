numbers_tuple = (1, 4, 2, 9, 33, 6)

numbers = list(numbers_tuple)

print(f'The tuple is {numbers_tuple}.')

index = int(input('Enter the index of an element:\n'))

numbers.remove(numbers[index])

print(f'The new tuple is {tuple(numbers)}.')