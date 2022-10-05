# coding: utf-8
# Ahian

def is_valid_radius(radius):
    try:
        if 0 < radius:
            return True
        else:
            raise ValueError("ERROR: Invalid radius!")
    except ValueError as err:
        return (err)
    except:
        return ("ERROR: Invalid radius!")

print(is_valid_radius(16))
print(is_valid_radius(-1))
print(is_valid_radius('12'))
print(is_valid_radius([16, 12]))
print(is_valid_radius(2.5))
print(is_valid_radius(0))