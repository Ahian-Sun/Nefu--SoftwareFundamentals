# coding: utf-8
# Ahian


import random

def bogo_sort(data):
    nums = 2
    is_sorted = False
    while not is_sorted:
        nums += 6
        i = 0
        while i < len(data) - 1:
            j = random.randrange(i, len(data))
            data[i], data[j] = data[j], data[i]
            i += 1
            nums += 4
        is_sorted = True
        i = 0
        while i < len(data) - 1:
            is_sorted = is_sorted and not data[i] > data[i + 1]
            i += 1
            nums += 3
    print("Number of operations: {}".format(nums))


