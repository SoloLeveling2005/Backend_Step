

class Airplane:
    def __init__(self,type_airplane, number_of_passengers_now,number_of_passengers_max):
        self.type_airplane = type_airplane
        self.number_of_passengers_now = number_of_passengers_now
        self.number_of_passengers_max = number_of_passengers_max

    def __eq__(self, other):
        if (self.type_airplane == other.type_airplane):
            return f"Типы равны, {self.type_airplane} == {other.type_airplane}"
        else:
            return f"Типы не равны, {self.type_airplane} !== {other.type_airplane}"

    def __add__(self, other):
        return self.number_of_passengers_now + other

    def __sub__(self, other):
        return self.number_of_passengers_now - other

    def __iadd__(self, other):
        self.number_of_passengers_now += other
        return self.number_of_passengers_now

    def __isub__(self, other):
        self.number_of_passengers_now -= other
        return self.number_of_passengers_now


    def __gt__(self, other):
        if (self.number_of_passengers_max > other.number_of_passengers_max):
            return f"Больше, {self.number_of_passengers_max} > {other.number_of_passengers_max}"
        else:
            return f"Не больше, {self.number_of_passengers_max} !> {other.number_of_passengers_max}"

    def __lt__(self, other):
        if (self.number_of_passengers_max < other.number_of_passengers_max):
            return f"Меньше, {self.number_of_passengers_max} < {other.number_of_passengers_max}"
        else:
            return f"Не меньше, {self.number_of_passengers_max} !< {other.number_of_passengers_max}"
    def __le__(self, other):
        if (self.number_of_passengers_max >= other.number_of_passengers_max):
            return f"Больше или равно, {self.number_of_passengers_max} >= {other.number_of_passengers_max}"
        else:
            return f"Не больше или равно, {self.number_of_passengers_max} !>= {other.number_of_passengers_max}"

    def __ge__(self, other):
        if (self.number_of_passengers_max <= other.number_of_passengers_max):
            return f"Меньше или равно, {self.number_of_passengers_max} <= {other.number_of_passengers_max}"
        else:
            return f"Не меньше или равно, {self.number_of_passengers_max} !<= {other.number_of_passengers_max}"

air1 = Airplane("one", 100, 1000)
air2 = Airplane("one", 500, 2000)
print(air1 == air2)
print("\n\n")


print(f"В самолете 1: теперь {air1 + 100} пассажиров")
print("\n\n")


print(f"В самолете 2: теперь {air2 - 200} пассажиров")
print("\n\n")

air2 += 400
print(f"В самолете 2: теперь {air2} пассажиров")
print("\n\n")


air2 -= 400
print(f"В самолете 2: теперь {air2} пассажиров")
print("\n\n")


print("Сравнение")
print("\n\n")


air1 = Airplane("one", 100, 1000)
air2 = Airplane("one", 500, 2000)
print(air1>air2)
print("\n\n")



print(air1<air2)
print("\n\n")



print(air1>=air2)
print("\n\n")



print(air1<=air2)
print("\n\n")


