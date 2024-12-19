import random

num_elements = int(input('Enter the number of elements in a set:\n'))
start = int(input('Enter the minimum integer:\n'))
end = int(input('Enter the maximum integer:\n'))

randomset = set()

for i in range(0, num_elements):
    randomset.add(random.randint(start, end))
print('Random set:', randomset)