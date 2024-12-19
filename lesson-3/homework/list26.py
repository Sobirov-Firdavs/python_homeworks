numbers = [1, 4, 2, 9, 33, 6]

print(f'The list is {numbers}.')

a = len(numbers) // 2

if len(numbers) % 2 == 0:
    print(f'The middle elements of the list are {numbers[a - 1 : a + 1]}')
else: print(f'The middle element of the list is {numbers[a]}.')