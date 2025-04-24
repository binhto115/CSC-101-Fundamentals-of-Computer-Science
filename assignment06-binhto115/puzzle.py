# Name: Binh To
# Date: 12/03/2022
# Github: 113943258
import sys
import read


try:
    file = sys.argv[1]
    read_puzzle = read.readPPM(file)
    for row in read_puzzle:
        for pixel in row:
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            if pixel[0] > 255:
                pixel[0] = 255
            pixel[0] *= 10
            pixel[1] = pixel[0]
            pixel[2] = pixel[1]
    hidden_image = open("hidden_image.ppm", "w")
    hidden_image.write("P3\n")
    height = len(read_puzzle)
    width = len(read_puzzle[0])
    hidden_image.write(f"{width} {height}\n")
    hidden_image.write("255\n")
    for row in read_puzzle:
        for pixel in row:
            for color in pixel:
                hidden_image.write(f"{color}\n")
    hidden_image.close()
except FileNotFoundError:
    print("ppm File does not exist")
except IndexError:
    print("The index of the inputted file is out of range")

