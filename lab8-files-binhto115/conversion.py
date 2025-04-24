# Name: Binh To
# Date: 11/07/2022
# Github: 113943258

from typing import Optional


def stringToFloat(input: str) -> Optional[float]:
    try:
        convertToFloat = float(input)
        print(convertToFloat)
        return convertToFloat
    except:
        print("It is not a floating point value")
        return None
