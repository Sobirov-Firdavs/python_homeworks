numbers = (4, 3, 2, 1, 0, 1, 2, 3, 4)

print(f'The tuple is {numbers}.')

a = int(input('How many elements do you want to join in a subtuple?\n'))

print('The subtuples are:')

for i in range(0, len(numbers), a):
    subtuple = numbers[i: i + a]
    print(subtuple)