# Name: Binh To
# Date: 10/24/2022
# GitHub: 113943258

import sys

if __name__ == "__main__":
    for i, j in enumerate(sys.argv):
        print(f"{i}: {j}")

    for i in range(len(sys.argv)):
        print(i, sys.argv[i])

