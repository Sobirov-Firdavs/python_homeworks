class account:
    def __init__(self, account_number, name, balance):
        self.id = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'{self.id}:[{self.name}, {self.balance}]'
    

class Bank:

    file_path = r'python_homeworks\lesson-8\homework\accounts.txt'

    def __init__(self):
        self.accounts = {}

    def add(self):
        try:
            id = max(self.accounts.keys()) + 1 if self.accounts else 101
            name = input('Enter your name: ')
            balance = int(input('Enter initial balance: '))
            self.accounts[id] = (name, balance)
            print(f'Created successfully! You account number is {id}.')
        except ValueError: print('ValueError occured. Please try again.')
    
    def view(self):
        try:
            id = int(input('Enter account number: '))
            if id in self.accounts.keys():
                print(f'Name: {self.accounts[id][0]}, Balance: {self.accounts[id][1]}')
                return
            print('Account not found.')
        except ValueError: print('ValueError occured. Please try again.')
        
    def deposit(self):
        try:
            id = int(input('Enter account number: '))
            if id in self.accounts.keys():
                deposit = int(input('Enter deposit amount: '))
                self.accounts[id][1] += deposit
                print('Deposit made successfully!')
                return
            print('Account not found.')
        except ValueError: print('ValueError occured. Please try again.')

    def withdraw(self):
        try:
            id = int(input('Enter account number: '))
            if id in self.accounts.keys():
                withdraw = int(input('Enter withdrawal amount: '))
                if self.accounts[id][1] > withdraw:
                    self.accounts[id][1] -= withdraw
                    print('Withdrawn successfully!')
                else: print('You do not have enough money to withdraw.')   
            else: print('Account with this number not found.')
        except ValueError: print('ValueError occured. Please try again.')

    def save(self):
        try:
            with open(self.file_path, 'w') as file:
                file.writelines(f'{account(k, v[0], v[1])}\n' for k, v in self.accounts.items())
                print('Saved successfully!')
        except FileNotFoundError: print('File not found.')

    def load(self):
        try:
            with open(self.file_path, 'r') as file:
                self.accounts = {}
                lines = file.readlines()
                for line in lines:
                    key, value = line.split(':')
                    key = int(key.strip())
                    value = value.replace('[', '').replace(']', '').strip('\n').split(', ')
                    self.accounts[key] = [value[0], int(value[1])]
                print('Loaded successfully!')
        except FileNotFoundError: print('File not found.')
    
    def menu(self):
        while True:
            print('''You have the following options:
1. Create account.
2. View account.
3. Make a deposit.
4. Withdraw money.
5. Save to file.
6. Load from file.
7. Exit''')
            option = input('Enter your option: ')
            if option == '1':
                self.add()
            elif option == '2':
                self.view()
            elif option == '3':
                self.deposit()
            elif option == '4':
                self.withdraw()
            elif option == '5':
                self.save()
            elif option == '6':
                self.load()
            elif option == '7':
                print('Good bye!')
                break
            else: print('Invalid option. Please try again.')

program = Bank()
program.menu()
        