string = input('Enter a word:\n')

length = len(string)
a = string.count('a')
e = string.count('e')
i = string.count('i')
u = string.count('u')
o = string.count('o')
A = string.count('A')
E = string.count('E')
I = string.count('I')
U = string.count('U')
O = string.count('O')

vowels = a + e + i + u + o + A + E + I + U + O
consonants = length - vowels

print(f'The string has {vowels} vowels and {consonants} consonants.')