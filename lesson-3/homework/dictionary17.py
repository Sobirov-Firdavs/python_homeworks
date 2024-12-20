dictionary = {
    'a' : 3,
    'b' : 4,
    'c' : 2,
    'd' : {
        'da' : 3,
        'db' : 4
    },
    'e' : 4,
    'f' : {
        'fa' : 5
    },
    'g' : 2 
}

values = [value for value in dictionary.values() if type(value) == dict]

print('Values that themselves are dictionaries:', values)