class Point:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return "Object Point: (%f, %f)" % (self.x, self.y)


class Circle:

    def __init__(self, center, radius: float):
        self.center = center
        self.radius = radius

    def __str__(self):
        return "Circle Attributes: (%f, %f)" % (self.center, self.radius)

