numbers = [1, 4, 2, 7, 9, 33, 6]

even = 0

for number in numbers:
    if number % 2 == 0:
        even +=1
    else: even = even
print(f'The list has {even} even numbers.')