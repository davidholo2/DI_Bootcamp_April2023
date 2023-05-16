from math import pi


class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError(
                "Please specify either the radius or diameter of the circle.")

    def area(self):
        return pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius


circle1 = Circle(radius=5)
circle2 = Circle(diameter=10)
circle3 = Circle(radius=3)
print(circle1.area())
print(circle1)
circle4 = circle1 + circle2
print(circle4.radius)
print(circle1 < circle2)
print(circle1 == circle2)
print(circle1 > circle2)

circles = [circle1, circle2, circle3, circle4]
sorted_circles = sorted(circles, key=lambda c: c.radius)
for circle in sorted_circles:
    print(circle)
