import src.Shape

class Rectangle(src.Shape.shape):
    def __init__(self, color, width, height):
        super().__init__(color=color)
        self.width = width
        self.height = height