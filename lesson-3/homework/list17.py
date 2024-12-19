list1 = [1, 4, 2]

print(f'The first list is {list1}.')

list2 = [7, 2, 33, 1]
print(f'The second list is {list2}.')

list1.extend(list2)

set1 = set(list1)

list3 = list(set1)

print(f'The combined list is {list3}.')