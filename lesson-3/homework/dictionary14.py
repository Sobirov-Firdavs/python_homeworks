dictionary = {
    'a' : 3,
    'b' : 4,
    'c' : 2,
    'd' : 7,
    'e' : 4,
    'f' : 2,
    'g' : 2 
}

target_value = int(input('Enter a value:\n'))

keys = [key for key, value in dictionary.items() if value == target_value]

print(keys)