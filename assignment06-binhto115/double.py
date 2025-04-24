# Name: Binh To
# Date: 12/03/2022
# Github: 113943258
import sys
import read

try:
    file = sys.argv[1]
    read_double = read.readPPM(file)
    outer_outer_list = []
    outer_list = []
    for row in read_double:
        new_row = []
        for column in row:
            double_column = column * 2
            new_row.append(double_column)
        outer_list.append(new_row)
    double = open("doubled.ppm", "w")
    height = len(read_double) * 2
    width = len(read_double[0]) * 2
    double.write("P3\n")
    double.write(f"{width} {height}\n")
    double.write("255\n")
    for row in outer_list:
        double_row = row * 2
        outer_outer_list.append(double_row)
    for row in outer_outer_list:
        for column in row:
            for color in column:
                double.write(f"{color}\n")
    double.close()
except FileNotFoundError:
    print("ppm file does not exist")
except IndexError:
    print("The index of the input file is out of range")
