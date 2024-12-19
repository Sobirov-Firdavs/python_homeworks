numbers = [1, 4, 2, 9, 33, 6]

print(f'The list is {numbers}.')

index = int(input('Enter the index of an element:\n'))

numbers.remove(numbers[index])

print(f'The new list is {numbers}.')