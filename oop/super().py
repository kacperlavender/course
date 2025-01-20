'''

super() = function used in a child class to call methods from parent class 
            (superclass).

            allows you to extend the functionality of the inherited methods

'''

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f'it is {self.color} and {'filled' if self.filled == True else 'not filled'}')

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled) # through super function we pass 
        self.radius = radius            # color and filled from Parent function

    def describe(self):
        print(f'it is a circle of an area of {3.14*self.radius*self.radius}')
        super().describe()

    '''
    if we have child and parent function - child method will get used 
    this is why we have to add super().describe() to have both descriptions
    '''


class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

    def describe(self):
        print(f'it is a square of an area of {self.width * self.width}')
        super().describe()


class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f'it is a traingle of an area of {0.5 * self.width * self.height}')
        super().describe()


circle = Circle(color="red", filled=True, radius=5)
square = Square(color="blue", filled=False, width=6)
triangle = Triangle(color="yellow", filled=True, width=7, height=8)

print(circle.color, circle.filled, circle.radius)
print(square.color, square.filled, square.width)
print(triangle.color, triangle.filled, triangle.width, triangle.height)

triangle.describe()