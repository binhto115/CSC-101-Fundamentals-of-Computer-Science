# Name: Binh To
# Date: 12/03/2022
# Github: 113943258
import sys
import read


try:
    file = sys.argv[1]
    read_sepia = read.readPPM(file)
    for row in read_sepia:
        for pixel in row:
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            new_red = 0.393 * red + 0.769 * green + 0.189 * blue
            new_green = 0.349 * red + 0.686 * green + 0.168 * blue
            new_blue = 0.272 * red + 0.534 * green + 0.131 * blue
            pixel[0] = int(new_red)
            pixel[1] = int(new_green)
            pixel[2] = int(new_blue)
            if pixel[0] > 255:
                pixel[0] = 255
            if pixel[1] > 255:
                pixel[1] = 255
            if pixel[2] > 255:
                pixel[2] = 255
    sepia = open("sepia.ppm", "w")
    sepia.write("P3\n")
    height = len(read_sepia)
    width = len(read_sepia[0])
    sepia.write(f"{width} {height}\n")
    sepia.write("255\n")
    for row in read_sepia:
        for pixel in row:
            for color in pixel:
                sepia.write(f"{color}\n")
    sepia.close()
except FileNotFoundError:
    print("ppm File does not exist")
except IndexError:
    print("The index of the inputted file is out of range")

