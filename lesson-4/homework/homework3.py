vowels = 'aioueAIOUE'

txt = input("Enter a string:\n")

newstring = ""
used = []

for i in range(len(txt)):
    newstring += txt[i]
    if (i + 1) % 3 == 0 and txt[i] not in vowels:
        if not newstring.endswith("_"):
            newstring += "_"

print(newstring)