dictionary = {
    'a' : 3,
    'b' : 4,
    'c' : 2,
    'd' : 7,
    'e' : 4,
    'f' : 2,
    'g' : 2 
}
new_dict = {key : value for key, value in dictionary.items() if value > 2}

print("Dictionary with values higher than 2:", new_dict)