n = int(input('Enter an integer: '))

state = True

for i in range(2, n):
    if n % i == 0:
        state = state and False
print(state)