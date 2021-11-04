import src.Rectangle

class Square(src.Rectangle.Rectangle):
    def __init__(self, color, length):
        super(Square, self).__init__(color=color, width=length, height=length)