class Shape:
    def __init__(self, w_rectangle=None, h_rectangle=None, circle_rad=None, right_triangle_footing=None,
                 right_triangle_height=None, trapezoid_h=None, trapezoid_a=None, trapezoid_b=None):
        self.w_rectangle = w_rectangle
        self.h_rectangle = h_rectangle
        self.circle_rad = circle_rad
        self.right_triangle_footing = right_triangle_footing
        self.right_triangle_height = right_triangle_height
        self.trapezoid_h = trapezoid_h
        self.trapezoid_a = trapezoid_a
        self.trapezoid_b = trapezoid_b

    def rectangle(self):
        return f"Площадь квадрата равна = {self.w_rectangle * self.h_rectangle}"

    def circle(self):
        S = 3.14 * (self.circle_rad ** 2)
        return f"Площадь круга равна = {S}"

    def right_triangle(self):
        S = (self.right_triangle_footing * self.right_triangle_height) / 2
        return f"Площадь правильного треугольника равна = {S}"

    def trapezoid(self):
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

cir = Circle(10).circle()
print(cir)

r_tr = Right_triangle(10, 20).right_triangle()
print(r_tr)

tr = Trapezoid(10, 20, 10).trapezoid()
print(tr)
