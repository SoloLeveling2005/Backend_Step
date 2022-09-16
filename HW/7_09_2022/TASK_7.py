import json


class Shape:
    def __init__(self, ellipse_coordinates_upper_corner_rectangle_described_around_it=None,
                 ellipse_rectangle_described_around_it_width=None, ellipse_rectangle_described_around_it_height=None,
                 ellipse_parallel_to_the_coordinate_axes=None, ellipse_rectangle_width=None,
                 ellipse_rectangle_height=None,
                 square_coordinates_upper_left_corner=None, square_length_side=None,
                 rectangle_coordinates_upper_left_corner=None,
                 rectangle_width=None, rectangle_height=None, circle_coordinates_upper_center=None, circle_radius=None,
                 param=None, params: list = None, url_doc: str = None):
        self.square_formula = "S=a*a"
        self.rectangle_formula = "S=a*b"
        self.circle_formula = "S=πR²"
        self.ellipse_formula = "(x**2)/(a**2)+(y**2)/(b**2)=1"

        # square
        self.square_coordinates_upper_left_corner = square_coordinates_upper_left_corner
        self.square_length_side = square_length_side

        # rectangle
        self.rectangle_coordinates_upper_left_corner = rectangle_coordinates_upper_left_corner
        self.rectangle_width = rectangle_width
        self.rectangle_height = rectangle_height

        # circle
        self.circle_coordinates_upper_center = circle_coordinates_upper_center
        self.circle_radius = circle_radius

        # ellipse
        self.ellipse_coordinates_upper_corner_rectangle_described_around_it = \
            ellipse_coordinates_upper_corner_rectangle_described_around_it
        self.ellipse_rectangle_described_around_it_width = ellipse_rectangle_described_around_it_width
        self.ellipse_rectangle_described_around_it_height = ellipse_rectangle_described_around_it_height
        self.ellipse_parallel_to_the_coordinate_axes = ellipse_parallel_to_the_coordinate_axes
        self.ellipse_rectangle_width = ellipse_rectangle_width
        self.ellipse_rectangle_height = ellipse_rectangle_height

        self.param = param
        self.params = params
        self.url_doc = url_doc

    def show(self):
        text = ""
        for i in self.param:
            text += f"{i} \n"
        return text

    def load(self):
        with open(self.url_doc, "r") as read_files:
            data = json.load(read_files)
        return data

    def square(self):
        self.data_square = [f"Координаты левого верхнего угла квадрата = {self.square_coordinates_upper_left_corner}",
                            f"длина стороны = {self.square_length_side}", f"Формула: {self.square_formula}"]
        return self.data_square

    def rectangle(self):
        self.data_rectangle = [
            f"Координаты левого верхнего угла прямоугольника = {self.rectangle_coordinates_upper_left_corner}",
            f"Длина прямоугольника = {self.rectangle_width}", f"Ширина прямоугольника = {self.rectangle_height}",
            f"Формула: {self.rectangle_formula}"]
        return self.data_rectangle

    def circle(self):
        self.data_circle = [f"Координаты центра окружности = {self.circle_coordinates_upper_center}",
                            f"Радиус окружности = {self.circle_radius}", f"Формула: {self.circle_formula}"]
        return self.data_circle

    def ellipse(self):
        self.data_ellipse = [
            f"Эллипс с заданными координатами верхнего угла описанного вокруг него прямоугольника = {self.ellipse_coordinates_upper_corner_rectangle_described_around_it}",
            f"Ширина данного прямоугольника = {self.ellipse_rectangle_described_around_it_width}",
            f"Длина данного прямоугольника = {self.ellipse_rectangle_described_around_it_height}",
            f"Оси ординат = {self.ellipse_parallel_to_the_coordinate_axes}",
            f"Ширина прямоугольника = {self.ellipse_rectangle_width}",
            f"Длина прямоугольника = {self.ellipse_rectangle_height}"]
        return self.data_ellipse

    def save(self):
        # data = {
        #     "square": self.data_square,
        #     "rectangle": self.data_rectangle,
        #     "circle": self.data_circle,
        #     "ellipse": self.data_ellipse
        # }
        data = []
        for i in self.params:
            data.append(i)
        with open("data_file.json", "w") as write_file:
            json.dump(data, write_file)


class Show(Shape):
    def __init__(self, param):
        super().__init__(param=param)


class Save(Shape):
    def __init__(self, params):
        super().__init__(params=params)


class Load(Shape):
    def __init__(self, url_doc):
        super().__init__(url_doc=url_doc)


class Square(Shape):
    def __init__(self, square_coordinates_upper_left_corner, square_length_side):
        super().__init__(square_coordinates_upper_left_corner=square_coordinates_upper_left_corner,
                         square_length_side=square_length_side)


class Rectangle(Shape):
    def __init__(self, rectangle_coordinates_upper_left_corner, rectangle_width, rectangle_height):
        super().__init__(rectangle_coordinates_upper_left_corner=rectangle_coordinates_upper_left_corner,
                         rectangle_width=rectangle_width, rectangle_height=rectangle_height)


class Circle(Shape):
    def __init__(self, circle_coordinates_upper_center, circle_radius):
        super().__init__(circle_coordinates_upper_center=circle_coordinates_upper_center, circle_radius=circle_radius)


class Ellipse(Shape):
    def __init__(self, ellipse_coordinates_upper_corner_rectangle_described_around_it,
                 ellipse_rectangle_described_around_it_width, ellipse_rectangle_described_around_it_height,
                 ellipse_parallel_to_the_coordinate_axes, ellipse_rectangle_width, ellipse_rectangle_height):
        super().__init__(
            ellipse_coordinates_upper_corner_rectangle_described_around_it=ellipse_coordinates_upper_corner_rectangle_described_around_it,
            ellipse_rectangle_described_around_it_width=ellipse_rectangle_described_around_it_width,
            ellipse_rectangle_described_around_it_height=ellipse_rectangle_described_around_it_height,
            ellipse_parallel_to_the_coordinate_axes=ellipse_parallel_to_the_coordinate_axes,
            ellipse_rectangle_width=ellipse_rectangle_width, ellipse_rectangle_height=ellipse_rectangle_height)


# Show
el = Square("12 32", 20).square()
sh = Show(param=el)
print(sh.show())
# Show
rec = Rectangle("12 32", 20, 10).rectangle()
sh = Show(param=rec)
print(sh.show())
# Show
cir = Circle("12 32", 20).circle()
sh = Show(param=cir)
print(sh.show())
# Show
cir = Ellipse("12 32", 20, 10, "12 34", 40, 30).ellipse()
sh = Show(param=cir)
print(sh.show())

# Save
cir = Ellipse("12 32", 20, 10, "12 34", 40, 30).ellipse()
rec = Rectangle("12 32", 20, 10).rectangle()
sh = Save(params=[cir, rec])
sh.save()

# Load
sh = Load(url_doc="data_file.json")
print(sh.load())
