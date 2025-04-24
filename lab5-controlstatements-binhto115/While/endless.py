# Name: Binh To
# Date: 10/19/2022
# GitHub: 113943258

if __name__ == "__main__": # This is to enable a "play" button in PyCharm
    value_1 = 0
    value_2 = 0
    while value_1 >= value_2:
        print("Performing an iteration of the loop:")
        print(f"Currently, value_1 = {value_1} and value_2 = {value_2}")
        value_1 += 1
        value_2 += 1
        # Add code here
        if value_1 == 101 and value_2 == 101:
            value_1 = value_1 // 10


