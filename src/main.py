# import src.Shape
# import src.Rectangle
import src
# from src import *
r = src.Rectangle.Rectangle("green", 5, 3)
s = src.Square.Square("blue", 5)
c = src.Circle.circle("red", 5)

print(r.color)
print(r.area())
print(r.perimeter())
print(bool(r))
print(abs(r))
print(r)

print("-"*50)

print(s.color)
print(s.area())
print(s.perimeter())
print(bool(s))
print(abs(s))
print(s)

print("-"*50)

print(c.color)
print(c.area())
print(c.perimeter())
print(bool(c))
print(abs(c))
print(c)
