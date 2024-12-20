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

boolean = any(isinstance(value, dict) for value in dictionary.values())

print('Contains nested dictionaries:', boolean)