import math


def get_area(radius):
    return math.pi * radius * radius


def get_circumference(radius):
    return 2 * math.pi * radius


radius = 20
print("Circumference of the circle is", get_circumference(20))
print("Area of the circle is", get_area(radius))








