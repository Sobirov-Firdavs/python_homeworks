a = input('Enter a number:\n')

last_digit1 = int(float(a) % 10)
last_digit2 = a[-1]

print(f'The last digit of the number in the integer part is {last_digit1}, and that in the decimal part is {last_digit2}.')