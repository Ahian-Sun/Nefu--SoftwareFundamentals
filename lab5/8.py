# coding: utf-8
# Ahian


import math
def get_volume(radius, height):
    try:
        if radius > 0 and height > 0:
            result = math.pi * radius ** 2 * height
            return ("%.f" %result)
        elif radius < 0 and height > 0:
            raise ValueError("ERROR: Radius must be positive.")
        elif radius > 0 and height < 0:
            raise ValueError("ERROR: Height must be positive.")
        elif radius < 0 and height < 0:
            raise ValueError("ERROR: Height and radius must be positive.")
        elif radius or height == 0:
            raise ValueError("ERROR: Not a cylinder.")
    except ValueError as e:
        return e
    except:
        return ('ERROR: Invalid input.')

print(get_volume(10, 2))
print(get_volume(-10, 2))
print(get_volume(10, -2))
print(get_volume(-10, -2))
print(get_volume(10, 0))
print(get_volume('ten', 2))
print(get_volume(1000, 2000))