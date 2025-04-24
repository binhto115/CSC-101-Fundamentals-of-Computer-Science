import math


def distance(p1, p2):
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


def circles_overlap(circle_1, circle_2):
    return distance(circle_1.center, circle_2.center) < (circle_1.radius + circle_2.radius)

