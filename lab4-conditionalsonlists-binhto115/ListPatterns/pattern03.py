# Name: Binh To
# Date: 10/14/2022
# Github: 113943258

input = ["A", "A", "A", "A", "B", "B", "B", "B"]
goal  = ["A", "C", "A", "C", "B", "D", "B", "D"]


def patternFunction(index: int, element: int) -> int:
    input[1] = "C"
    input[3] = "C"
    input[5] = "D"
    input[7] = "D"
    return input[index]
