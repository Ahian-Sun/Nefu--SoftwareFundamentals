# coding: utf-8
# Ahian


def binary_search(numbers, value):
    max_index = len(numbers) - 1
    min_index = 0
    while (min_index <= max_index):
        mid = (min_index + max_index)//2
        if numbers[mid] == value:
            return mid
            break
        elif numbers[mid] < value:
            min_index = mid + 1
        elif numbers[mid] > value:
            max_index = mid - 1
    return -1

numbers = [10, 15, 20, 27, 41, 69]
print(binary_search(numbers, 69))

numbers = [13, 18, 54, 61, 78, 93]
print(binary_search(numbers, 10))