list1 = ['a', 'b', 'c']

print(f'The first list is {list1}.')

list2 = ['c', 'f', 'a', 'v']
print(f'The second list is {list2}.')

list1.extend(list2)

print(f'The merged list is {list1}.')