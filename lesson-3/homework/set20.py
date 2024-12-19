set1 = {2, 4, 8, 12, 3}
set2 = {3, 6, 23, 5, 4}

intersection = set1 & set2

print(f'The first set is {set1}.')
print(f'The second set is {set2}.')

if intersection == set():
    print('The sets do not have anything in common.')
else: print(f'They have {intersection} in common.')