def convert_cel_to_far():
    cel1 = float(input('Enter a temperature in degrees Celsius: '))
    far1 = round(cel1 * 9 / 5 + 32, 2)
    print(f'It is equal to {far1} degrees Fahrenheit.')

def convert_far_to_cel():
    far2 = float(input('Enter a temperature in degrees Fahrenheit: '))
    cel2 = round((far2 - 32) * 5 / 9, 2)
    print(f'It is equal to {cel2} degrees Fahrenheit.')

convert_cel_to_far()
convert_far_to_cel()