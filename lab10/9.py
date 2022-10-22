# coding: utf-8
# Ahian


def no_evens(numbers):
    if len(numbers) == 1 and numbers[0] % 2 == 1:
        return True
    elif numbers[0] % 2 == 0:
        return False
    elif numbers[0] % 2 == 1:
        return no_evens(numbers[1:])


print(no_evens([5, 3, 5, 6]))

print(no_evens([2]))

print(no_evens([1, 3, 5, 7]))