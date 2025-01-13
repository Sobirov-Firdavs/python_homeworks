class account:
    def __init__(self, account_number, name, balance):
        self.id = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'{self.id}:[{self.name}, {self.balance}]'

file_path = r'python_homeworks\lesson-8\homework\accounts.txt'

with open(file_path, 'r') as file:
    accounts = {}
    lines = file.readlines()
    for line in lines:
        acc = account(*line)
        print(f'Name: {acc.name}')