# @property = Decorator used to define a method as a property (is can be acces like an atribute)
#       Benefit: Add additional logic when read, write or delete atributes
#       Gives you getter, setter, and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("height must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("width has been deleted")

        
    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")

rect = Rectangle(3, 4)


rect.width = 5
rect.height = 5

del rect.width
del rect.height


print(rect.width)
print(rect.height)