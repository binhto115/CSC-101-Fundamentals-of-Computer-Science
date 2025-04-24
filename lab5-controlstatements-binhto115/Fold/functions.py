# Name: Binh To
# Date: 10/19/2022
# Github: 113943258

import objects
Point = objects.Point


def getMinimum(p: list[int]) -> int:
    minimum_num = p[0]
    for i in p:
        if i < minimum_num:
            minimum_num = i
    return minimum_num


def areAllTrue(p: list[bool]) -> bool:
    if all(i is True for i in p):
        return True
    else:
        return False


def getCenterPoint(p: list[Point]) -> Point:
    list_x = []
    list_y = []
    for i in p:
        point_x = i.x
        list_x.append(point_x)
        point_y = i.y
        list_y.append(point_y)
    total_x_inputs = len(list_x)
    total_y_inputs = len(list_y)
    average_x = sum(list_x) / total_x_inputs
    average_y = sum(list_y) / total_y_inputs
    average_point = Point(average_x, average_y)
    return average_point


def countLessThanFour(p: list[str]) -> int:
    list_of_str_less_than_4 = []
    for i in p:
        if len(i) < 4:
            list_of_str_less_than_4.append(i)
    num_str_less_than_4 = len(list_of_str_less_than_4)
    return num_str_less_than_4


