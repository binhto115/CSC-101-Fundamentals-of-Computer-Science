# Name: Binh To
# Date: 10/13/2022
# Github: 113943258

import math


class Duration:
    """Represents a length of time in minutes and whole seconds."""
    def __init__(self, minutes: int, seconds: int):
        self.minutes = minutes
        self.seconds = seconds

    def __repr__(self):
        return f"Duration({self.minutes},{self.seconds})"

    def __eq__(self, other):
        return (other is self or
                type(other) == Duration and
                self.minutes == other.minutes and
                self.seconds == other.seconds)


class Song:
    def __init__(self, name: str, artist: str, length: Duration):
        self.name = name
        self.artist = artist
        self.length = length

    def __repr__(self):
        return f"Duration({self.name},{self.artist}, {self.length})"

    def __eq__(self, other):
        return (other is self or
                type(other) == Song and
                self.name == other.name and
                self.artist == other.artist and
                self.length == other.length)


class Point:
    """Represents an 2d cartesian coordinate point."""
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x},{self.y})"

    def __eq__(self, other):
        return (other is self or
                type(other) == Point and
                math.isclose(self.x, other.x) and
                math.isclose(self.y, other.y))


class Rectangle:
    """Represents rectangle defined by top-left and bottom-right points."""
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def __repr__(self):
        return f"Rectangle({self.top_left},{self.bottom_right})"

    def __eq__(self, other):
        return (other is self or
                type(other) == Rectangle and
                self.top_left == other.top_left and
                self.top_left == other.top_left)


class Triangle:
    """Represents Triangle defined by three points."""
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return f"Triangle({self.a},{self.b},{self.c})"

    def __eq__(self, other):
        return (other is self or
                type(other) == Triangle and
                self.a == other.a and
                self.b == other.b and
                self.c == other.c)


# Part 1:
def isShorterThan(p1: Duration, p2: Duration) -> bool:
    second_1_mod = p1.seconds % 60
    second_1_floor_division = p1.seconds // 60
    minute_1 = p1.minutes + second_1_floor_division

    second_2_mod = p2.seconds % 60
    second_2_floor_division = p2.seconds // 60
    minute_2 = p2.minutes + second_2_floor_division

    if minute_1 < minute_2 and second_1_mod < second_2_mod:
        return True
    elif minute_1 < minute_2 and second_1_mod > second_2_mod:
        return True
    elif minute_1 == minute_2 and second_1_mod < second_2_mod:
        return True
    elif minute_1 == minute_2 and second_1_mod > second_2_mod:
        return False
    elif minute_1 == minute_2 and second_1_mod == second_2_mod:
        return False
    else:
        return False


# Part 2:
def triangulateRectangle(p: Rectangle) -> list[Triangle]:

    left_point_x = p.top_left.x
    left_point_y = p.top_left.y
    bottom_right_x = p.bottom_right.x
    bottom_right_y = p.bottom_right.y

    top_left_points = Point(left_point_x, left_point_y)
    bottom_right_points = Point(bottom_right_x, bottom_right_y)

    top_right_points = Point(bottom_right_x, left_point_y)
    bottom_left_points = Point(left_point_x, bottom_right_y)

    a_tri = top_left_points
    b_tri = top_right_points
    c_tri = bottom_right_points
    d_tri = bottom_left_points
    tri_points_1 = Triangle(a_tri, b_tri, c_tri)
    tri_points_2 = Triangle(a_tri, c_tri, d_tri)
    return [tri_points_1, tri_points_2]


# Part 3:
def createRectangle(p1: Point, p2: Point) -> Rectangle:
    if p1.x < p2.x and p1.y > p2.y:
        smallest_x_4 = p1.x
        biggest_y_4 = p1.y
        biggest_x_4 = p2.x
        smallest_y_4 = p2.y
        new_top_left_point_4 = Point(smallest_x_4, biggest_y_4)
        new_bottom_right_point_4 = Point(biggest_x_4, smallest_y_4)
        return Rectangle(new_top_left_point_4, new_bottom_right_point_4)

    if p1.x > p2.x and p1.y < p2.y:
        smallest_x_3 = p2.x
        biggest_y_3 = p2.y
        biggest_x_3 = p1.x
        smallest_y_3 = p1.y
        new_top_left_point_3 = Point(smallest_x_3, biggest_y_3)
        new_bottom_right_point_3 = Point(biggest_x_3, smallest_y_3)
        return Rectangle(new_top_left_point_3, new_bottom_right_point_3)

    if p1.x > p2.x and p1.y > p2.y:
        smallest_x = p2.x
        biggest_y = p1.y
        biggest_x = p1.x
        smallest_y = p2.y
        new_top_left_point = Point(biggest_x, biggest_y)
        new_bottom_right_point = Point(smallest_x, smallest_y)
        return Rectangle(new_top_left_point, new_bottom_right_point)

    if p1.x < p2.x and p1.x < p2.x:
        smallest_x_2 = p1.x
        biggest_y_2 = p2.y
        biggest_x_2 = p2.x
        smallest_y_2 = p2.y
        new_top_left_point_2 = Point(smallest_x_2, biggest_y_2)
        new_bottom_right_point_2 = Point(biggest_x_2, smallest_y_2)
        return Rectangle(new_top_left_point_2, new_bottom_right_point_2)


# Part 5:
def addDurations(p1: Duration, p2: Duration) -> Duration:
    duration_minutes = p1.minutes + p2.minutes
    duration_seconds = p1.seconds + p2.seconds
    duration_seconds_floor_division = duration_seconds // 60
    duration_seconds_modulo = duration_seconds % 60
    new_duration_minutes = duration_minutes + duration_seconds_floor_division
    new_time = Duration(new_duration_minutes, duration_seconds_modulo)
    return new_time


# Part 6:
def getLengthsInSeconds(p: list[Song]) -> list[int]:
    song_lengths = []
    for i in p:
        song_length_minutes = i.length.minutes
        song_length_seconds = i.length.seconds
        song_lengths_in_seconds = song_length_minutes * 60 + song_length_seconds
        song_lengths.append(song_lengths_in_seconds)
    return song_lengths


# Part 7:
def getSongsByArtist(p1: list[Song], p2: str) -> list[Song]:
    song_list = []
    for i in p1:
        song_name = i.name
        song_artist = i.artist
        song_min = i.length.minutes
        song_sec = i.length.seconds
        song_duration = Duration(song_min, song_sec)
        if song_artist == p2:
            song_input = Song(song_name, song_artist, song_duration)
            song_list.append(song_input)
    return song_list


# Part 8:
def getPlaylistLength(p: list[Song]) -> Duration:
    duration_min_list = []
    duration_sec_list = []
    for i in p:
        song_min = i.length.minutes
        duration_min_list.append(song_min)
        song_sec = i.length.seconds
        duration_sec_list.append(song_sec)

    duration_sec_list_floor_division = sum(duration_sec_list) // 60
    duration_sec_list_modulo = sum(duration_sec_list) % 60

    new_duration_min = sum(duration_min_list) + duration_sec_list_floor_division
    total_duration = Duration(new_duration_min, duration_sec_list_modulo)
    return total_duration
