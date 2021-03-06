from abc import ABC , abstractmethod
class shape(ABC):

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"{self.__class__.__name__}'s color is {self.color}"

    def __bool__(self):
        return 2 > 5

    @abstractmethod
    def __abs__(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
