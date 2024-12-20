person = {
    'name' : 'Firdavs',
    'email' : 'jdhnjh@gmail.com',
    'age' : 20
}

print(person)
removed = input('Enter a key to remove:\n')

if removed in person:
    del person[removed]
    print(f'New dictionary:\n{person}')
else: print('The key entered does not exist in the dictionary.')