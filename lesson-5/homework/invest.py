def invest(amount, rate, years):

    for i in range(years):
        amount = amount * (1 + rate)
        print(f'Year {i + 1}: ${round(amount, 2)}')

amount = float(input('Enter an initial amount: '))
rate = float(input('Enter an annual rate in percentage: ')) / 100.00
years = int(input('Enter years for the amount of investment to be calculated for: '))

invest(amount, rate, years)