def factors(integer):
    for i in range (1, integer + 1):
        if integer % i == 0:
            print(f'{i} is a factor of {integer}.')

factors(int(input('Enter an integer: ')))