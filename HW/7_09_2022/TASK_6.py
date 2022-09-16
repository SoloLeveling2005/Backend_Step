class Shape:

    def __init__(self, w_rectangle=None, h_rectangle=None, circle_rad=None, right_triangle_footing=None,
                 right_triangle_height=None, trapezoid_h=None, trapezoid_a=None, trapezoid_b=None, *args):
        self.w_rectangle = w_rectangle
        self.h_rectangle = h_rectangle
        self.circle_rad = circle_rad
        self.right_triangle_footing = right_triangle_footing
        self.right_triangle_height = right_triangle_height
        self.trapezoid_h = trapezoid_h
        self.trapezoid_a = trapezoid_a
        self.trapezoid_b = trapezoid_b
        self.shape = ""

    def __str__(self):
        if self.shape == "circle":
            return f"Информация: Радиус круга = {self.circle_rad}, формула: S=πR²"
        elif self.shape == "rectangle":
            return f"Информация: Ширина прямоугольника = {self.w_rectangle}, высота прямоугольника = " \
                   f"{self.h_rectangle}, формула: S=ab "
        elif self.shape == "right_triangle":
            return f"Информация: Основание правильного треугольника = {self.right_triangle_footing}, высота " \
                   f"правильного треугольника = {self.right_triangle_height}, формула: S=½bh"
        elif self.shape == "trapezoid":
            return f"Информация: Высота трапеции = {self.trapezoid_h}, основание один = " \
                   f"{self.trapezoid_a} основание два = {self.trapezoid_b}, формула: S=½h(a+b)"

    def rectangle(self):
        if type(self.w_rectangle) == str or type(self.h_rectangle) == str:
            self.shape = "rectangle"
            return self.__str__()
        else:
            return f"Площадь квадрата равна = {self.w_rectangle * self.h_rectangle}"

    def circle(self):
        if type(self.circle_rad) == str:
            self.shape = "circle"
            return self.__str__()
        else:
            S = 3.14 * (self.circle_rad ** 2)
            return f"Площадь круга равна = {S}"

    def right_triangle(self):
        if type(self.right_triangle_footing) == str or type(self.right_triangle_height) == str:
            self.shape = "right_triangle"
            return self.__str__()
        else:
            S = (self.right_triangle_footing * self.right_triangle_height) / 2
            return f"Площадь правильного треугольника равна = {S}"

    def trapezoid(self):
        if type(self.trapezoid_h) == str or type(self.trapezoid_a) == str or type(self.trapezoid_b) == str:
            self.shape = "trapezoid"
            return self.__str__()
        else:
            S = self.trapezoid_h * (self.trapezoid_a + self.trapezoid_b)
            return f"Площадь трапеции равна = {S}"


class Rectangle(Shape):
    def __init__(self, w_rectangle, h_rectangle):
        super().__init__(w_rectangle=w_rectangle, h_rectangle=h_rectangle)


class Circle(Shape):
    def __init__(self, circle_rad):
        super().__init__(circle_rad=circle_rad)


class Right_triangle(Shape):
    def __init__(self, right_triangle_footing, right_triangle_height):
        super().__init__(right_triangle_footing=right_triangle_footing, right_triangle_height=right_triangle_height)


class Trapezoid(Shape):
    def __init__(self, trapezoid_h, trapezoid_a, trapezoid_b):
        super().__init__(trapezoid_h=trapezoid_h, trapezoid_a=trapezoid_a, trapezoid_b=trapezoid_b)


sq = Rectangle(10, 20).rectangle()
print(sq)
print("")
sq = Rectangle("10", 20).rectangle()
print(sq)
print("\n\n")

cir = Circle("10").circle()
print(cir)
print("")
cir = Circle(10).circle()
print(cir)
print("\n\n")


r_tr = Right_triangle(10, 20).right_triangle()
print(r_tr)
print("")
r_tr = Right_triangle(10, "20").right_triangle()
print(r_tr)
print("\n\n")

tr = Trapezoid(10, 20, 10).trapezoid()
print(tr)
print("")
tr = Trapezoid(10, "20", 10).trapezoid()
print(tr)