class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"it is {self.color} and {"filed" if self.filled else "not filled"}")


class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"It is a square with an area of {self.width*self.width}cm^2")


class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It is a triangle with an area of {0.5 * self.width * self.height}cm^2")



circle = Circle(color="red", filled=True, radius=5)
square = Square(color="blue", filled=False, width=6)
triangle = Triangle(color="black", filled=True, width=7, height=8)

triangle.describe()