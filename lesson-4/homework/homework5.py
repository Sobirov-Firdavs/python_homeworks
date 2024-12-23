p = input('Enter a password:\n')

i = 0

if len(p) > 7:
    while i < len(p):
        letter = p[i]
        if letter == letter.upper():
            print('Password is strong.')
            break
        else: i+=1
    else: print('Password must contain an uppercase letter.')
else: print('Password is too short.')