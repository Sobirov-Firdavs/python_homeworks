import random
n = 0

while n < 10:
    if n == 0:
        n += 1
        i = random.randint(1, 100)
        guess = int(input('Guess an integer:\n'))
        if guess > i:
            print('Too high!')
        elif guess < i:
            print('Too low!')
        else:
            print('You guessed it right!')
            break
    elif n < 9:
        n += 1
        guess = int(input('Guess an integer:\n'))
        if guess > i:
            print('Too high!')
        elif guess < i:
            print('Too low!')
        else:
            print('You guessed it right!')
            break
    else:
        guess = int(input('Guess an integer:\n'))
        if guess ==  i:
            print('You guessed it right!')
        elif input('You lost. Want to play again?\n') in ['Y', 'YES', 'y', 'yes', 'ok', 'OK']:
            n = 0