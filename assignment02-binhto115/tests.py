# Name: Binh To
# Date: 10/13/2022
# Github: 113943258

import unittest
import math
import hw2


class AssignmentTests(unittest.TestCase):
    # The following test must not be modified and pass
    def test_Duration_init_1(self):
        duration = hw2.Duration(60, 0)
        self.assertEqual(duration.minutes, 60)
        self.assertEqual(duration.seconds, 0)

    def test_Duration_init_2(self):
        duration = hw2.Duration(0, 30)
        self.assertEqual(duration.minutes, 0)
        self.assertEqual(duration.seconds, 30)

    def test_Duration_init_3(self):
        duration = hw2.Duration(15, 15)
        self.assertEqual(duration.minutes, 15)
        self.assertEqual(duration.seconds, 15)

    def test_Duration_eq_1(self):
        duration = hw2.Duration(60, 0)
        self.assertEqual(duration, duration)

    def test_Duration_eq_2(self):
        duration_1 = hw2.Duration(60, 0)
        duration_2 = hw2.Duration(60, 0)
        self.assertEqual(duration_1, duration_2)

    def test_Duration_eq_3(self):
        duration = hw2.Duration(60, 0)
        point = hw2.Point(60, 0)
        self.assertNotEqual(duration, point)

    def test_Point_init_1(self):
        point = hw2.Point(5, 5)
        self.assertEqual(point.x, 5)
        self.assertEqual(point.y, 5)

    def test_Point_init_2(self):
        point = hw2.Point(0, 10)
        self.assertEqual(point.x, 0)
        self.assertEqual(point.y, 10)

    def test_Point_init_3(self):
        point = hw2.Point(10, 0)
        self.assertEqual(point.x, 10)
        self.assertEqual(point.y, 0)

    def test_Point_eq_1(self):
        point = hw2.Point(15, 15)
        self.assertEqual(point, point)

    def test_Point_eq_2(self):
        point_1 = hw2.Point(15, 15)
        point_2 = hw2.Point(15, 15)
        self.assertEqual(point_1, point_2)

    def test_Point_eq_3(self):
        point = hw2.Point(15, 15)
        duration = hw2.Duration(15, 15)
        self.assertNotEqual(point, duration)

    def test_Rectangle_init_1(self):
        rectangle = hw2.Rectangle(hw2.Point(0, 5), hw2.Point(5, 0))
        self.assertEqual(rectangle.top_left.x, 0)
        self.assertEqual(rectangle.top_left.y, 5)
        self.assertEqual(rectangle.bottom_right.x, 5)
        self.assertEqual(rectangle.bottom_right.y, 0)

    def test_Rectangle_eq_1(self):
        rectangle = hw2.Rectangle(hw2.Point(0, 5), hw2.Point(5, 0))
        self.assertEqual(rectangle, rectangle)

    def test_Rectangle_eq_2(self):
        rectangle_1 = hw2.Rectangle(hw2.Point(0, 5), hw2.Point(5, 0))
        rectangle_2 = hw2.Rectangle(hw2.Point(0, 5), hw2.Point(5, 0))
        self.assertEqual(rectangle_1, rectangle_2)

    def test_Rectangle_eq_3(self):
        rectangle = hw2.Rectangle(hw2.Point(0, 0), hw2.Point(5, 0))
        duration = hw2.Duration(15, 15)
        self.assertNotEqual(rectangle, duration)

    def test_Triangle_init_1(self):
        triangle = hw2.Triangle(hw2.Point(0, 0), hw2.Point(5, 5), hw2.Point(10, 0))
        self.assertEqual(triangle.a.x, 0)
        self.assertEqual(triangle.a.y, 0)
        self.assertEqual(triangle.b.x, 5)
        self.assertEqual(triangle.b.y, 5)
        self.assertEqual(triangle.c.x, 10)
        self.assertEqual(triangle.c.y, 0)

    def test_Triangle_eq_1(self):
        triangle = hw2.Triangle(hw2.Point(0, 0), hw2.Point(5, 5), hw2.Point(10, 0))
        self.assertEqual(triangle, triangle)

    def test_Triangle_eq_2(self):
        triangle_1 = hw2.Triangle(hw2.Point(0, 0), hw2.Point(5, 5), hw2.Point(10, 0))
        triangle_2 = hw2.Triangle(hw2.Point(0, 0), hw2.Point(5, 5), hw2.Point(10, 0))
        self.assertEqual(triangle_1, triangle_2)

    def test_Triangle_eq_3(self):
        triangle = hw2.Triangle(hw2.Point(0, 0), hw2.Point(5, 5), hw2.Point(10, 0))
        duration = hw2.Duration(15, 15)
        self.assertNotEqual(triangle, duration)

    # Implement your tests here:
    def test_isShorterThan(self):
        time_1 = hw2.Duration(10, 60)
        time_2 = hw2.Duration(11, 30)
        self.assertTrue(hw2.isShorterThan(time_1, time_2), True)

        time_3 = hw2.Duration(12, 60)
        time_4 = hw2.Duration(11, 30)
        self.assertFalse(hw2.isShorterThan(time_3, time_4), True)

        time_5 = hw2.Duration(12, 00)
        time_6 = hw2.Duration(12, 00)
        self.assertFalse(hw2.isShorterThan(time_5, time_6), True)

        time_7 = hw2.Duration(5, 60)
        time_8 = hw2.Duration(4, 50)
        self.assertFalse(hw2.isShorterThan(time_7, time_8), True)

    def test_triangulateRectangle(self):
        top_left = hw2.Point(1, 5)
        bottom_right = hw2.Point(5, 1)
        rectangle_points = hw2.Rectangle(top_left, bottom_right)

        point_1 = hw2.Point(1, 5)
        point_2 = hw2.Point(5, 5)
        point_3 = hw2.Point(5, 1)

        point_4 = hw2.Point(1, 5)
        point_5 = hw2.Point(5, 1)
        point_6 = hw2.Point(1, 1)
        list_check = [hw2.Triangle(point_1, point_2, point_3), hw2.Triangle(point_4, point_5, point_6)]
        self.assertEqual(hw2.triangulateRectangle(rectangle_points), list_check)

        top_left_2 = hw2.Point(1, 5)
        bottom_right_2 = hw2.Point(3, 2)
        rectangle_points_2 = hw2.Rectangle(top_left_2, bottom_right_2)

        point_7 = hw2.Point(1, 5)
        point_8 = hw2.Point(3, 5)
        point_9 = hw2.Point(3, 2)

        point_10 = hw2.Point(1, 5)
        point_11 = hw2.Point(3, 2)
        point_12 = hw2.Point(1, 2)
        list_check_2 = [hw2.Triangle(point_7, point_8, point_9), hw2.Triangle(point_10, point_11, point_12)]
        self.assertEqual(hw2.triangulateRectangle(rectangle_points_2), list_check_2)

    def test_createRectangle(self):
        test_point_1 = hw2.Point(4, 2)
        test_point_2 = hw2.Point(3, 1)
        point_1 = hw2.Point(4, 2)
        point_2 = hw2.Point(3, 1)
        rectangle_1 = hw2.Rectangle(point_1, point_2)
        self.assertEqual(hw2.createRectangle(test_point_1, test_point_2), rectangle_1)

        test_point_3 = hw2.Point(3, 1)
        test_point_4 = hw2.Point(4, 2)
        point_3 = hw2.Point(3, 2)
        point_4 = hw2.Point(4, 1)
        rectangle_2 = hw2.Rectangle(point_3, point_4)
        self.assertEqual(hw2.createRectangle(test_point_3, test_point_4), rectangle_2)

        test_point_5 = hw2.Point(4, 1)
        test_point_6 = hw2.Point(2, 3)
        point_5 = hw2.Point(2, 3)
        point_6 = hw2.Point(4, 1)
        rectangle_3 = hw2.Rectangle(point_5, point_6)
        self.assertEqual(hw2.createRectangle(test_point_5, test_point_6), rectangle_3)

        test_point_7 = hw2.Point(2, 3)
        test_point_8 = hw2.Point(4, 1)
        point_7 = hw2.Point(2, 3)
        point_8 = hw2.Point(4, 1)
        rectangle_4 = hw2.Rectangle(point_7, point_8)
        self.assertEqual(hw2.createRectangle(test_point_7, test_point_8), rectangle_4)

    def test_addDurations(self):
        point_1 = hw2.Duration(6, 60)
        point_2 = hw2.Duration(7, 60)
        add_points = hw2.Duration(15, 00)
        self.assertEqual(hw2.addDurations(point_1, point_2), add_points)

        point_3 = hw2.Duration(10, 50)
        point_4 = hw2.Duration(5, 60)
        add_points = hw2.Duration(16, 50)
        self.assertEqual(hw2.addDurations(point_3, point_4), add_points)

    def test_Song_init_1(self):
        # First Test:
        song_duration_1 = hw2.Duration(3, 26)
        song = hw2.Song("Black", "G-Dragon and Jennie", song_duration_1)
        self.assertEqual(song.name, "Black")
        self.assertEqual(song.artist, "G-Dragon and Jennie")
        self.assertEqual(song.length, song_duration_1)

        # Second Test:
        song_duration_2 = hw2.Duration(3, 38)
        song_2 = hw2.Song("Black Swan", "BTS", song_duration_2)
        self.assertEqual(song_2.name, "Black Swan")
        self.assertEqual(song_2.artist, "BTS")
        self.assertEqual(song_2.length, song_duration_2)

    def test_Song_eq_1(self):
        # First Test:
        song_duration_1 = hw2.Duration(4, 00)
        song_duration_2 = hw2.Duration(4, 00)
        song_1 = hw2.Song("Gales of Song", "Belle", song_duration_1)
        song_2 = hw2.Song("Gales of Song", "Belle", song_duration_2)
        self.assertEqual(song_1, song_2)

        # Second Test:
        song_duration = hw2.Duration(2, 34)
        song = hw2.Song("No Idea", "Don Toliver", song_duration)
        self.assertEqual(song, song)


    def test_getLengthsInSeconds(self):
        song_duration = hw2.Duration(4, 43)
        song_duration_2 = hw2.Duration(4, 8)
        song_1 = hw2.Song("Let You Down", "David Podsiadlo", song_duration)
        song_2 = hw2.Song("I REALLY WANT TO STAY AT YOUR HOUSE",
                          "Rosa Walton & Hallie Coggins", song_duration_2)
        input_song = [song_1, song_2]
        song_list_duration = [283, 248]
        self.assertEqual(hw2.getLengthsInSeconds(input_song), song_list_duration)

        song_duration_3 = hw2.Duration(3, 42)
        song_duration_4 = hw2.Duration(5, 24)
        song_duration_5 = hw2.Duration(5, 31)
        song_3 = hw2.Song("eight", "IU", song_duration_3)
        song_4 = hw2.Song("Isabella's Lullaby", "The Promised Neverland OST", song_duration_4)
        song_5 = hw2.Song("ONLY", "LeeHi", song_duration_5)
        input_song_2 = [song_3, song_4, song_5]
        song_list_duration_2 = [222, 324, 331]
        self.assertEqual(hw2.getLengthsInSeconds(input_song_2), song_list_duration_2)


    def test_getSongByArtist(self):
        song_duration_1 = hw2.Duration(3, 1)
        input_song_1 = hw2.Song("Who", "Lauv", song_duration_1)
        song_duration_2 = hw2.Duration(8, 2)
        input_song_2 = hw2.Song("A Million Miles Away", "Belle", song_duration_2)
        song_duration_3 = hw2.Duration(3, 18)
        input_song_3 = hw2.Song("I Like Me Better", "Lauv", song_duration_3)

        test_duration_1 = hw2.Duration(3, 1)
        test_input_song_1 = hw2.Song("Who", "Lauv", test_duration_1)
        test_duration_3 = hw2.Duration(3, 18)
        test_input_song_3 = hw2.Song("I Like Me Better", "Lauv", test_duration_3)
        self.assertEqual(hw2.getSongsByArtist([input_song_1, input_song_2, input_song_3], "Lauv"), [test_input_song_1,
                                                                                                    test_input_song_3])
        song_duration_4 = hw2.Duration(3, 44)
        input_song_4 = hw2.Song("Dynamite", "BTS", song_duration_4)
        song_duration_5 = hw2.Duration(3, 56)
        input_song_5 = hw2.Song("HOME", "BTS", song_duration_5)
        song_duration_6 = hw2.Duration(5, 19)
        input_song_6 = hw2.Song("FAKE LOVE", "BTS", song_duration_6)

        test_duration_4 = hw2.Duration(3, 44)
        test_input_song_4 = hw2.Song("Dynamite", "BTS", test_duration_4)
        test_duration_5 = hw2.Duration(3, 56)
        test_input_song_5 = hw2.Song("HOME", "BTS", test_duration_5)
        test_duration_6 = hw2.Duration(5, 19)
        test_input_song_6 = hw2.Song("FAKE LOVE", "BTS", test_duration_6)
        self.assertEqual(hw2.getSongsByArtist([input_song_4, input_song_5, input_song_6], "BTS"),
                         [test_input_song_4, test_input_song_5, test_input_song_6])



    def test_getPlaylistLength(self):
        duration_1 = hw2.Duration(5, 16)
        duration_2 = hw2.Duration(3, 38)
        song_1 = hw2.Song("Natsu No Yuki", "krage", duration_1)
        song_2 = hw2.Song("0 (zero) - English version", "LMYK", duration_2)
        total_duration = hw2.Duration(8, 54)
        self.assertEqual(hw2.getPlaylistLength([song_1, song_2]), total_duration)

        duration_3 = hw2.Duration(3, 46)
        duration_4 = hw2.Duration(3, 23)
        duration_5 = hw2.Duration(4, 7)
        song_3 = hw2.Song("Chuyen Doi Ta", "Da LAB", duration_3)
        song_4 = hw2.Song("K/DA - POP/STARS", "Madison Beer, (G)I-DLE, Jaira Burns", duration_4)
        song_5 = hw2.Song("drivers license", "Olivia Rodrigo", duration_5)
        total_duration_2 = hw2.Duration(11, 16)
        self.assertEqual(hw2.getPlaylistLength([song_3, song_4, song_5]), total_duration_2)


if __name__ == "__main__":
    unittest.main()
