import math

class Circle:
    def __init__(self, radius):
        if not type(radius) is int and not type(radius) is float:
            raise TypeError("radius must be a number")
        if not (radius >= 0 and radius <= 1000):
            raise ValueError("radius must be between 0 and 1000 inclusive")
        self.radius = radius

    def area(self):
        return round(math.pi * (self.radius ** 2), 2)

    def circumference(self):
        return round(2 * math.pi * self.radius, 2)
