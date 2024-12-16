string = input('Enter a string:\n')

words = string.split()

acronym = ''

for word in words:
    acronym += word[0].upper()
print(acronym)