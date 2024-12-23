list1 = []
len1 = int(input('How many elements do you want to have in the 1st list?\n'))
print('Include them one-by-one:')

for i in range(len1):
    a = input(f'Element number {i + 1}: ')
    list1.append(a)

list2 = []
len2 = int(input('How many elements do you want to have in the 2nd list?\n'))
print('Include them one-by-one:')

for j in range(len2):
    b = input(f'Element number {j + 1}: ')
    list2.append(b)

uncommon = []

for n in range(len1):
    if not list1[n] in list2:
        uncommon.append(list1[n])

for m in range(len2):
    if not list2[m] in list1:
        uncommon.append(list2[m])

print(f'The uncommon elements are {uncommon}.')