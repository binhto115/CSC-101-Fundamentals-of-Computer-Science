import math


# Part 1
class Price:
    def __init__(self, dollars: int, cents: int):
        self.dollars = dollars
        self.cents = cents

    def __str__(self):
        return "$" + str(self.dollars) + "." + str(self.cents)

    def __eq__(self, other):
        return (other is self or
                type(other) == Price and
                self.dollars == other.dollars and self.cents == other.cents)


# This function takes the two inputted prices and returns the sum of the two prices
# The parameters are type Price
# The function return is type int
def add_prices(p1: Price, p2: Price):
    dollars = p1.dollars + p2.dollars
    cents = p1. cents + p2.cents
    new_cents = cents // 100
    new_cents_2 = cents % 100
    new_dollars = dollars + new_cents
    price_total = Price(new_dollars, new_cents_2)
    return price_total


# write your function here
# Part 2 and Part 3:
class Point:
    # This function initializes the object's attributes
    # The parameters are type float
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # This __eq__ function allows comparisons between two x's and two y's
    # The parameters are type Point
    # The function return is type float
    def __eq__(self, other):
        same_x = math.isclose(self.x, other.x)
        same_y = math.isclose(self.y, other.y)
        return type(other) == Point and same_x and same_y


class Rectangle:
    # This function initializes the object's attributes from class Point
    # The parameters are type Point
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right

    # This function allows comparisons two top_lefts and two bottom_rights
    # The parameters are type Rectangle
    # The function return is type int
    def __eq__(self, other):
        return (type(other) is Rectangle and
                self.top_left == other.top_left and
                self.bottom_right == other.bottom_right)


class Circle:
    # This function initializes the object's attributes from class Point
    # The parameters are type Point and type float, respectively
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    # This function allows comparisons between two centers and two radii
    # The parameters are type Circle
    # The function return is type float
    def __eq__(self, other):
        return (type(other) is Circle and
                self.center == other.center and
                self.radius == other.radius)


# Part 4:
# This function takes the points from the class Rectangle and returns the perimeter of a rectangle
# The Parameter is type Rectangle
# The function return is type int and type float
def rectangle_perimeter(p: Rectangle):
    return (abs(p.top_left.x - p.bottom_right.x) * 2 +
            abs(p.top_left.y - p.bottom_right.y) * 2)


# This function takes points from the class Rectangle
# and returns four points that represents the lower half of a rectangle
# The Parameter is type Rectangle
# The function return is type float
# Part 5:
def rectangle_lower_half(p: Rectangle):
    old_top_left_x = p.top_left.x
    old_bottom_right_x = p.bottom_right.x

    old_top_left_y = p.top_left.y
    old_bottom_right_y = p.bottom_right.y

    new_top_y = (abs(old_top_left_y - old_bottom_right_y) / 2) + p.bottom_right.y
    original_bottom_right_point = (old_bottom_right_x, old_bottom_right_y)
    new_top_left_point = (old_top_left_x, new_top_y)
    final = (new_top_left_point, original_bottom_right_point)
    return final


# Part 6:
# This function takes points from the class Rectangle and returns True if the width and length are equal
# To prove if the rectangle is a square
# The parameter is type Rectangle
# The function return is type bool
def is_square(p: Rectangle) -> bool:
    width = abs(p.top_left.x - p.bottom_right.x) * 2
    length = abs(p.top_left.y - p.bottom_right.y) * 2
    return width == length


# Part 7:
# This function takes points from the Circle class and the Rectangle class
# and checks if the inputted circle is completely inside the inputted rectangle
# The parameters are type Circle and Rectangle
# The function return is type bool
def circle_within_rectangle(p1: Circle, p2: Rectangle) -> bool:
    top_left_x = p2.top_left.x
    bottom_right_x = p2.bottom_right.x
    top_left_y = p2.top_left.y
    bottom_right_y = p2.bottom_right.y
    perimeter_width = abs(top_left_x - bottom_right_x)
    perimeter_length = abs(top_left_y - bottom_right_y)
    circle_radius = p1.radius
    circle_center_x = p1.center.x
    circle_center_y = p1.center.y
    return (top_left_x < circle_center_x < bottom_right_x and
            bottom_right_y < circle_center_y < top_left_y and
            circle_radius < perimeter_width and
            circle_radius < perimeter_length)


# Part 8:
# This function takes points from the Rectangle class and returns the circle's centered points and its radius
# The parameter is type Rectangle
# The function return is type float
def circle_bound(p: Rectangle):
    length = abs(p.top_left.x - p.bottom_right.x) / 2
    width = abs(p.top_left.y - p.bottom_right.y) / 2
    new_length = p.top_left.x + length
    new_width = p.bottom_right.y + width
    circle_center = Point(new_length, new_width)
    circle_radius = math.sqrt((p.bottom_right.x - new_length) ** 2 +
                              (p.bottom_right.y - new_width) ** 2)
    circle = Circle(circle_center, circle_radius)
    return circle

def f(a:int, b:str) -> bool:
    x = a**a
    if x == 27 and b in ['a', 'b', 'c']:
        return True
    return False
print(f(3, "b"))



