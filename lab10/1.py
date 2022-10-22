# coding: utf-8
# Ahian


def count_down(n):
    if n > 0:
        print(n)
        count_down(n-1)
    elif n == 0:
        print('Go!')

count_down(6)