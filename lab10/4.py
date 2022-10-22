# coding: utf-8
# Ahian


def print_between(start, end):
    if start <= end:
        print(start,end=" ")
        print_between(start+1, end)

print_between(-9, 5)