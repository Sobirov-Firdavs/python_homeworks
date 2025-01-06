def check(func):
    def wrapper():
        try:
            return func()
        except ZeroDivisionError:
            print('Denominator cannot be zero.')
    return wrapper

@check
def div():
    a = int(input('Enter a numerator: '))
    b = int(input('Enter a denominator: '))
    return a / b

result = div()
if result is not None:
    print('Result:', result)