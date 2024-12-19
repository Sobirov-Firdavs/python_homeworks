numbers = (5, 4, 3, 2, 1, 0, 1, 2, 3, 8, 5)

print(f'The tuple is {numbers}.')

if numbers == numbers[::-1]:
    print('The tuple is palinrome.')
else: print('The tuple is not palindrome.')