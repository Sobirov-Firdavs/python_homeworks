lists = [[1, 3, 5], [3, 9, 0], [3, 4, 7]]

print(f'The list has three sublists: {lists}.')
sublist = int(input('Enter the ordinal number of a sublist:\n'))

print(f'The smallest number in the sublist is {min(lists[sublist - 1])}.')