import math


def square(side):

    area = side * side
    if not float(side).is_integer():
        return math.ceil(area)
    return int(area)


side = 2.5
area = square(side)
print(f"сторона {side} → площадь {area}")
