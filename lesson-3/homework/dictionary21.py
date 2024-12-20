dictionary = {
    'd': 3,
    'b': 4,
    'a': 2,
    'c': 7,
}

new_dictionary = {key: dictionary[key] for key in sorted(dictionary, key = dictionary.get)}

print('Original dictionary:\n', dictionary)
print('New dictionary:\n', new_dictionary)