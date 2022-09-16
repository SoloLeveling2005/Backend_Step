class Flat:
    def __init__(self, S, price):
        self.S = S
        self.price = price

    def __eq__(self, other):
        if (self.S == other.S):
            return f"Площади равны ==, {self.S} == {other.S}"
        else:
            return f"Площади не равны ==, {self.S} != {other.S}"

    def __ne__(self, other):
        if (self.S != other.S):
            return f"Площади не равны != , {self.S} != {other.S}"
        else:
            return f"Площади равны != , {self.S} == {other.S}"

    def __gt__(self, other):
        if (self.price > other.price):
            return f"Больше, {self.price} > {other.price}"
        else:
            return f"Не больше, {self.price} !> {other.price}"

    def __lt__(self, other):
        if (self.price < other.price):
            return f"Меньше, {self.price} < {other.price}"
        else:
            return f"Не меньше, {self.price} !< {other.price}"

    def __le__(self, other):
        if (self.price >= other.price):
            return f"Больше или равно, {self.price} >= {other.price}"
        else:
            return f"Не больше или равно, {self.price} !>= {other.price}"

    def __ge__(self, other):
        if (self.price <= other.price):
            return f"Меньше или равно, {self.price} <= {other.price}"
        else:
            return f"Не меньше или равно, {self.price} !<= {other.price}"


fl1 = Flat(300, 50000)
fl2 = Flat(900, 120000)

print(fl1 == fl2)
print("\n\n")

print(fl1 != fl2)
print("\n\n")

print(fl1 > fl2)
print("\n\n")

print(fl1 < fl2)
print("\n\n")

print(fl1 >= fl2)
print("\n\n")

print(fl1 <= fl2)
print("\n\n")
