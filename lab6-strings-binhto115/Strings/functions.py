# Name: Binh To
# Date: 10/24/2022
# GitHub: 113943258

def swapCase(input: str) -> str:
    new_string = ""
    for i in input:
        if 97 <= ord(i) <= 122:
            new_string += chr(ord(i) - 32)
        elif 65 <= ord(i) <= 90:
            new_string += chr(ord(i) + 32)
        else:
            new_string += i
    return new_string


def replaceChar(input: str, search: str, replace: str) -> str:
    new_string = ""
    if len(search) > 1 or len(replace) > 1:
        return input
    for i in input:
        if i == search:
            i = replace
            new_string += i
        else:
            new_string += i
    return new_string

