# Name: Binh To
# Date: 10/19/2022
# GitHub: 113943258

if __name__ == "__main__": # This is to enable a "play" button in PyCharm
    # You will calculate the average of this list
    values = [3.33, 45.0, 12.5, 80.0, 45.0, 16.0]

    # Write your code here
    n = 0
    storage = []
    while n < len(values):
        storage.append(values[n])
        n += 1
        if n == 6:
            average = sum(storage) / len(values)
            print(average)

