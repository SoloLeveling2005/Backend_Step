class Circle:

    def __init__(self, r=0, c=0):
        """
        R = С/(2*π)
        С = 2π*r
        где C — длина окружности.
        """
        self.C = c
        self.r = r
        self.pi = 3.14

        self.R = self.C / (2 * self.pi)
        self.C = 2 * self.pi * self.r

    def __eq__(self, other):

        if (self.R == other.R):
            return f"Равны, {self.R} == {other.R}"
        else:
            return f"Не равны, {self.R} == {other.R}"

    def __gt__(self, other):
        if (self.C > other.C):
            return f"Больше, {self.C} > {other.C}"
        else:
            return f"Не больше, {self.C} !> {other.C}"

    def __le__(self, other):
        if (self.C >= other.C):
            return f"Больше или равно, {self.C} >= {other.C}"
        else:
            return f"Не больше или равно, {self.C} !>= {other.C}"

    def __ge__(self, other):
        if (self.C <= other.C):
            return f"Меньше или равно, {self.C} <= {other.C}"
        else:
            return f"Не меньше или равно, {self.C} !<= {other.C}"

    def __add__(self, other):
        return f"+ {2 * self.pi * (self.r + other.r)}"

    def __sub__(self, other):
        return f"- {2 * self.pi * (self.r - other.r)}"

    def __iadd__(self, other):
        self.r += other.r
        return f"+= {2 * self.pi * self.r}"

    def __isub__(self, other):
        self.r -= other.r
        return f"-= {2 * self.pi * self.r}"



print("\n\n")

circ1 = Circle(c=10)
circ2 = Circle(c=20)
print(circ1 == circ2)

print("\n\n")

circ1 = Circle(r=10)
circ2 = Circle(r=20)
print(circ1 > circ2)

print("\n\n")

circ1 = Circle(r=10)
circ2 = Circle(r=20)
print(circ1 <= circ2)

print("\n\n")

circ1 = Circle(r=10)
circ2 = Circle(r=20)
print(circ1 >= circ2)

print("\n\n")

circ1 = Circle(r=10)
circ2 = Circle(r=20)

print(circ1+circ2)

print("\n\n")

circ1 = Circle(r=10)
circ2 = Circle(r=20)

print(circ1-circ2)

print("\n\n")

circ1 = Circle(r=10)
circ2 = Circle(r=20)
circ1 += circ2
print(circ1)


print("\n\n")

circ1 = Circle(r=10)
circ2 = Circle(r=20)
circ1 -= circ2
print(circ1)