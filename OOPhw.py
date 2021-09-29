import math

class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return d

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        s = (y2-y1)/(x2-x1)
        return s

class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        pi = math.pi
        v = pi * self.radius * self.radius * self.height
        return v

    def surface_area(self):
        pi = math.pi
        a = (2 * pi * self.radius * self.height) + (2 * pi * self.radius * self.radius)
        return a


bob = Line((3, 2), (8, 10))
c = Cylinder(2, 3)

print(bob.slope())
print(bob.distance())
print(c.volume())
print(c.surface_area())
