numbers = [4, 3, 2, 1, 0, 1, 2, 3, 4]

print(f'The list is {numbers}.')

a = int(input('How many sublists do you want to divide the list into?\n'))

print('The sublists are:')

for i in range(0, len(numbers), a):
    sublists = numbers[i: i + a]
    print(sublists)