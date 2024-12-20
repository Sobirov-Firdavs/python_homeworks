person = {
    'name' : 'Firdavs',
    'lname' : 'Sobirov',
    'email' : 'jdhnjh@gmail.com'
}

value = input('Enter a value:\n')

value_number = 0

for i in person.values():
    if i == value:
        value_number += 1
print(f'{value} appears {value_number} times in the dictionary.')