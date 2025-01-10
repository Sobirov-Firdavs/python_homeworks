import math

class Vector:
    
    def __init__(self, vector: list):
        self.vector = vector

    def __len__(self):
        return len(self.vector)

    def __iter__(self):
        return self
    
    def __str__(self):
        return str(self.vector)
    

    """Addition"""
    def __add__(self, other):
        dimen = self.__len__()
        if dimen == other.__len__():
            added = Vector([self.vector[i] + other.vector[i] for i in range(dimen)])
            return f'{self.vector} + {other.vector} = {added.vector}'
        else: print('The vectors should be in the dimension.')

    """Substruction"""
    def __sub__(self, other):
        dimen = self.__len__()
        if dimen == other.__len__():
            substracted = Vector([self.vector[i] - other.vector[i] for i in range(dimen)])
            return f'{self.vector} - {other.vector} = {substracted.vector}'
        else: print('The vectors should be in the dimension.')

    """Dot product"""
    def dot_product(self, other):
        dimen = self.__len__()
        if dimen == other.__len__():
            dot_product = Vector(sum(self.vector[i] * other.vector[i] for i in range(dimen)))
            return f'{self.vector} * {other.vector} = {dot_product.vector}'
        else: print('The vectors should be in the dimension.')

    """Scalar Multiplication"""
    def scalar_mult(self):
        dimen = self.__len__()
        factor = 3
        scalar_mult_product = Vector([self.vector[i] * factor for i in range(dimen)])
        return f'{self.vector} * {factor} = {scalar_mult_product.vector}'
    
    """Magnitude"""
    def magnitude(self):
        dimen = self.__len__()
        magnitude = round(math.sqrt(sum(self.vector[i] ** 2 for i in range(dimen))), 3)
        return magnitude
    
    """Normalization"""
    def normalize(self):
        dimen = self.__len__()
        magnitude = math.sqrt(sum(self.vector[i] ** 2 for i in range(dimen)))
        v_unit = [round(self.vector[i] / magnitude, 3) for i in range(dimen)]
        return v_unit
    

vector1 = Vector([1, 2, 3])
vector2 = Vector([4, 5, 6])
print('Vector:', vector1)
print('Addition:', vector1.__add__(vector2))
print('Substraction:', vector1.__sub__(vector2))
print('Dot product: ', vector1.dot_product(vector2))
print('Scalar multiplication:', vector1.scalar_mult())
print('The magnitude of the vector:', vector1.magnitude())
print('Normalization:', vector1.normalize())