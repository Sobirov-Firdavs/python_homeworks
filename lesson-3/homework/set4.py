set1 = {2, 4, 8, 5, 3}
set2 = {3, 5, 2}

print(f'The first set is {set1}.')
print(f'The second set is {set2}.')

if set1 - set2 == set() or set2 - set1 == set():
    print(f'One set is a subset of the other.')
else: print('No one of them is a subset of the other.')