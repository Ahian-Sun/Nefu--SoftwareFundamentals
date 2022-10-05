# coding: utf-8
# Ahian

def get_max(numbers):
    try:
        k = max(numbers)
        return float(k)
    except:
        return ("ERROR: Invalid number!")

print(get_max([3, -2, 'two', 4, 'one']))
print(get_max([3, -2, 1, 4]))