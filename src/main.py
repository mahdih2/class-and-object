# import src.Shape
# import src.Rectangle
import src
# from src import *
r = src.Rectangle.Rectangle("green", 5, 3)
s = src.Square.Square("blue", 5)
c = src.Circle.circle("red", 5)

my_list = [r, s, c]

for i in my_list:
    print(i.color)
    print(i.area())
    print(i.perimeter())
    print(bool(i))
    print(abs(i))
    print(i)
    print("-"*50)