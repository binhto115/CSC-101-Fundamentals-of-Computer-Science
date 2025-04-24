# Name: Binh To
# Date: 10/14/2022
# Github: 113943258


def areTwoEqual(l: list, index_1: int, index_2: int) -> bool:
    if l[index_1] == l[index_2]:
        return True


def sumOfThree(l: list) -> float:
    list_length = len(l)
    if list_length == 3:
        return l[0] + l[1] + l[2]
    else:
        return 0


def sumOfUpToThree(l: list) -> float:
    list_length = len(l)
    if list_length == 3 or list_length > 3:
        return l[0] + l[1] + l[2]
    elif list_length < 3:
        return sum(l[:2])


def getFromFirstAsIndex(l: list) -> int:
    first_index = l[0]
    return l[first_index]

