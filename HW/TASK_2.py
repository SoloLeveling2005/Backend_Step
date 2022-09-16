import cmath

class Complex:
    def __init__(self, a, b):

        self.a = a
        self.b = b
        self.z = complex(self.a, self.b)

    def __add__(self, other):
        return complex(self.a, self.b) + complex(other.a, other.b)

    def __sub__(self, other):
        return complex(self.a, self.b) - complex(other.a, other.b)

    def __mul__(self, other):
        return complex(self.a, self.b) * complex(other.a, other.b)

    def __truediv__(self, other):
        return complex(self.a, self.b) / complex(other.a, other.b)


comp1 = Complex(7, -8)
comp2 = Complex(7, -8)
print(comp1+comp2)

print("\n\n")

print(comp1-comp2)

print("\n\n")

print(comp1*comp2)

print("\n\n")

print(comp1/comp2)

print("\n\n")


# Если честно я так до конца и непонял что тут происходит