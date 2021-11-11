# import src.Shape
import src.Shape

class Rectangle(src.Shape.shape):
    def __init__(self, color, width, height):
        super().__init__(color=color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2*self.height + 2*self.width

    def __abs__(self):
        return (self.width ** 2 + self.height **2) ** 0.5