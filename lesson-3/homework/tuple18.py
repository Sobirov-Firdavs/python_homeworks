numbers = ((-5, -4, -3), (-2, -1), (0, 1, 2, 3), (4, 5, 6))

print(f'The tuple is {numbers}.')

index = int(input('Enter an index:\n'))

print(f'The smallest in the subtuple with the index {index} is {min(numbers[index])}.')