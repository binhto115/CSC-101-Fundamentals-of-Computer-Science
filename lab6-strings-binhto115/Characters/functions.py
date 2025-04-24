# Name: Binh To
# Date: 10/24/2022
# GitHub: 113943258

def isEnglishUpper(c: str) -> bool:
    for i in c:
        if chr(65) <= i[0] <= chr(90):
            return True
        else:
            return False
