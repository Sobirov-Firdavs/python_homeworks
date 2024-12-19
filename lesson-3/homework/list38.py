numbers = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5]

print(f'The list is {numbers}.')

if numbers == numbers[::-1]:
    print('The list is palinrome.')
else: print('The list is not palindrome.')