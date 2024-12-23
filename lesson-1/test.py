while True:
    a = int(input('a = '))
    b = int(input('b = '))

    operation = input('Choose: (+, -, *, /)\n')

    if operation == '+':
        print(f'a + b = {a + b}')
    elif operation == '-':
        print(f'a - b = {a - b}')

    q = input('Do you want run again?\n')
    if q.lower() in ['q', 'quit', 'no', 'n']:
        print('Good bye!')
        break
