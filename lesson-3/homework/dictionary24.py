tuple = (('a', 3), ('b', 2), ('c', 8))

keys = list(tuple[i][0] for i in range(0, len(tuple)))
values = list(tuple[i][1] for i in range(0, len(tuple)))

dictionary = dict(zip(keys, values))

print(dictionary)