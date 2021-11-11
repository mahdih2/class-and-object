import src.Shape as sS

class circle(sS.shape):
    def __init__(self, color, radios):
        super().__init__(color=color)
        self.radios = radios

    def __abs__(self):
        pass

    def area(self):
        return 3.14 * self.radios ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radios

