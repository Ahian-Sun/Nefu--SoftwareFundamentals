# coding: utf-8
# Ahian


def get_max_list(numbers):
    if len(numbers) == 1:
        return numbers[0]
    elif numbers[0] > numbers[1]:
        numbers[1] = numbers[0]
        return get_max_list(numbers[1:])
    elif numbers[0] < numbers[1]:
        return get_max_list(numbers[1:])

lst = [1, 4, 5, -9]
print(get_max_list(lst))

lst = [1]
print(get_max_list(lst))