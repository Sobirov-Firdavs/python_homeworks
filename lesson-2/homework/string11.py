string = input('Enter a string:\n')


digit1 = string.count('1')
digit2 = string.count('2')
digit3 = string.count('3')
digit4 = string.count('4')
digit5 = string.count('5')
digit6 = string.count('6')
digit7 = string.count('7')
digit8 = string.count('8')
digit9 = string.count('9')
digit0 = string.count('0')

digits = digit0 + digit1 + digit2 + digit3 + digit4 + digit5 + digit6 + digit7 + digit8 + digit9

print(f'The string contains {digits} digits.')