person = {
    'name' : 'Firdavs',
    'email' : 'jdhnjh@gmail.com',
    'age' : 20
}

key = input('Enter a key:\n')

if key in person:
    print(f'{key} is available in the dictionary.')
else: print('There is no such a key.')