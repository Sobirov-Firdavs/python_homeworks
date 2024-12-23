import random

things = ['paper', 'rock', 'scissors']

c = 0
u = 0

while True:
    computer = random.choice(things)
    user = input('Choose: (rock, paper, scissors)\n')
    if c < 5 or u < 5:
        if computer == user:
            print(f'Computer also chose {computer}.')
        elif computer == 'rock' and user == 'paper':
            print(f'Computer chose {computer}, and you are winner.')
            u += 1
        elif computer == 'scissors' and user == 'rock':
            print(f'Computer chose {computer}, and you are winner.')
            u += 1
        elif computer == 'paper' and user == 'scissors':
            print(f'Computer chose {computer}, and you are winner.')
            u += 1
        else: 
            print(f'Computer chose {computer}, and you are loser.')
            c += 1
    else:
        if c > u: print('The computer won this game.')
        else: print('You won this game.')
    break