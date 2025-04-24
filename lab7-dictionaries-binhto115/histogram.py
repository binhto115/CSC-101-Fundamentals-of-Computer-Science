# Name: Binh To
# Date: 10/25/2022
# Github: 113943258


def getHistogram(input: str) -> dict[str, int]:
    dict_list = {}
    list_of_keys = []
    split_input = input.split(" ")
    for i in split_input:
        list_of_keys.append(i)
    print("The sorted list is " + str(list_of_keys))
    for j in list_of_keys:
        if j not in dict_list:
            dict_list[j] = 1
        else:
            dict_list[j] += 1
    print(dict_list)
    return dict_list
