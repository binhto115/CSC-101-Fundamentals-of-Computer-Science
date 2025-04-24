import math


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        same_x = math.isclose(self.x, other.x)
        same_y = math.isclose(self.y, other.y)
        return type(other) is Point and same_x and same_y

