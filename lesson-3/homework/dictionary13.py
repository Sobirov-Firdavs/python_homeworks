person = {
    'name' : 'Firdavs',
    'lname' : 'Sobirov',
    'email' : 'jdhnjh@gmail.com'
}
swapped = {value: key for key, value in person.items()}

print(f'Original:\n{person}\nSwapped:\n{swapped}')