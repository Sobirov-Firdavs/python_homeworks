person = {
    'name' : 'Firdavs',
    'email' : 'jdhnjh@gmail.com',
    'age' : 20
}

key = input('Enter a key:\n')

if key in person:
    print(f'{key} is {person[key]}.')
else: print('There is no such a key.')