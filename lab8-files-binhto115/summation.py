# Name: Binh To
# Date: 11/07/2022
# Github: 113943258

import sys
print(sys.argv)

if len(sys.argv) < 2:
    print("The file cannot be opened")
    exit()
elif len(sys.argv) == 0:
    print("The argument is not provided")
    exit()

file_input = 0
try:
    file = sys.argv[1]
    file_input = open(file, "r")
except FileNotFoundError:
    print("File not Found")
except IndexError:
    print("Out of range")
    exit()

for line in file_input:
    try:
        split_num = line.split()
        sum_of_num = float(split_num[0]) + float(split_num[1])
        print(sum_of_num)
    except IndexError:
        print("Missing a value in the text file")
    except ValueError:
        print("A string could not be converted to float")
file_input.close()



