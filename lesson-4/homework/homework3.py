noo = 'aioueAIOUE'

txt = input("Enter a string:\n")

newstring = ''

counter = 0

for i in range(len(txt)):
    counter += 1
    newstring += txt[i]
    if i != len(txt) - 1 and counter >= 3 and txt[i] not in noo:
        noo += txt[i]
        newstring += '_'
        counter = 0

print(newstring)