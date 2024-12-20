dictionary = {
    'd' : 3,
    'b' : 4,
    'a' : 2,
    'c' : 7,
}

keys = list(dictionary.keys())

keys.sort()

new_dictionary = {key : dictionary[key] for key in keys}

print('Original dictionary:\n', dictionary)
print('New dictionary:\n', new_dictionary)