class shape(object):

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"{self.__class__.__name__}'s color is {self.color}"
