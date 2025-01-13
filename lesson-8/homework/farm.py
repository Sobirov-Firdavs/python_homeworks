class animal:
    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number

    def __str__(self):
        return f'This animal is {self.name}.'
    
    def display_number(self):
        print(f'There are {self.number} of them in the farm.')

class wild(animal):
    def __init__(self, name, number, home, meat):
        super().__init__(name, number)
        self.home = home
        self.meat = meat
        
    def come_from(self):
        print(f'{self.name} comes from {self.home}.')

    def meat_amount(self):
        print(f'{self.name} eats {self.meat} kg of meat a day.')

class tame(animal):
    def __init__(self, name, number, year):
        super().__init__(name, number)
        self.year = year
        
    def domesticate(self):
        print(f'{self.name} has been domesticated in {self.year}.')

class fish(animal):
    def __init__(self, name, number):
        super().__init__(name, number)

    @staticmethod
    def spec_do():
        print('Fish can swim.')

animal1 = wild('Lion', 5, 'Africa', 30)
animal2 = tame('Horse', 20, 1200)
animal3 = fish('Shark', 4)

print(animal1)
animal1.display_number()
animal1.come_from()
animal1.meat_amount()
print(animal2)
animal2.display_number()
animal2.domesticate()
print(animal3)
animal3.display_number()
animal3.spec_do()