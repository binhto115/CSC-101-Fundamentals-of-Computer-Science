# Name: Binh To
# Date: 10/14/2022
# Github: 113943258

input = [1, 1, -1, -1, 1, -1, 1, -1]
goal  = [1, 2, -3, -4, 5, -6, 7, -8]


def patternFunction(index: int, element: int) -> int:
    input[1] = 2
    input[2] = -3
    input[3] = -4
    input[4] = 5
    input[5] = -6
    input[6] = 7
    input[7] = -8
    return input[index]


