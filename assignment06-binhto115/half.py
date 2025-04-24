# Name: Binh To
# Date: 12/03/2022
# Github: 113943258
import sys
import read

try:
    file = sys.argv[1]
    read_half = read.readPPM(file)
    outer_list = []
    for row in range(0, len(read_half), 2):
        new_row = []
        for column in range(0, len(read_half[row]), 2):
            pixel_1 = read_half[row][column]
            pixel_2 = read_half[row][column + 1]
            pixel_3 = read_half[row + 1][column]
            pixel_4 = read_half[row + 1][column + 1]
            red_avg = (pixel_1[0] + pixel_2[0] + pixel_3[0] + pixel_4[0]) // 4
            green_avg = (pixel_1[1] + pixel_2[1] + pixel_3[1] + pixel_4[1]) // 4
            blue_avg = (pixel_1[2] + pixel_2[2] + pixel_3[2] + pixel_4[2]) // 4
            pixel = [red_avg, green_avg, blue_avg]
            new_row.append(pixel)
        outer_list.append(new_row)
    half = open("halfed.ppm", "w")
    height = len(read_half) // 2
    width = len(read_half[0]) // 2
    half.write("P3\n")
    half.write(f"{width} {height}\n")
    half.write("255\n")
    for row in outer_list:
        for column in row:
            for color in column:
                half.write(f"{color}\n")
    half.close()
except FileNotFoundError:
    print("ppm file does not exist")
except IndexError:
    print("The index of the input file is out of range")

