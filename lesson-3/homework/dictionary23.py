dict1 = {
    'a' : 3,
    'b' : 4,
    'c' : 2,
    'd' : 7,
}

dict2 = {
    'e' : 4,
    'f' : 2,
    'a' : 2,
    'b' : 5
}

dict1_set = set(dict1.keys())
dict2_set = set(dict2.keys())

print(f'Common keys in the two dictionaries are: {dict1_set & dict2_set}.')