numbers = [1, 4, 2, 7, 9, 33, 6]

odd = 0

for number in numbers:
    if number % 2 == 1:
        odd +=1
    else: odd = odd
print(f'The list has {odd} odd numbers.')