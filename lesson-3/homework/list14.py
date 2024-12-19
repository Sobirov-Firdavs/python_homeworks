list1 = [1, 98, 4, 8]
list2 = []

a = input('We have 2 lists: list1 and list2. Choose one them:\n')

if a == 'list1':
    if list1 == []:
        print('The list chosen is empty.')
    else: print('The list chosen is not empty.')
elif a == 'list2':
    if list2 == []:
        print('The list chosen is empty.')
    else: print('The list chosen is not empty.')
else: print('Type correctly!')