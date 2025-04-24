# Returns the largest number out of the two values
def max_101(n: float, m: float) -> float:
    num_n = float(n)
    num_m = float(m)
    if num_n > num_m:
        return num_n
    else:
        return num_m


# Return the largest number of the three inputted values
def max_of_three(x: float, y: float, z: float) -> float:
    num_x = float(x)
    num_y = float(y)
    num_z = float(z)
    if num_x > num_y and num_x > num_z:
        return num_x
    elif num_y > num_x and num_y > num_z:
        return num_y
    else:
        return num_z


# Return $ per every late date
def rental_late_fee(days: int) -> int:
    late_day = int(days)
    if late_day > 24:
        return 100
    elif 15 < late_day <= 24:
        return 19
    elif 9 < late_day <= 15:
        return 7
    elif 0 < late_day <= 9:
        return 5
    else:
        return 0

