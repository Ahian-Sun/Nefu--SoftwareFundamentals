# coding: utf-8
# Ahian


def shifting(data, index):
    item_to_check = data[index]
    i = index - 1
    while i >= 0 and data[i] > item_to_check:
        data[i+1] = data[i]
        i -= 1
        data[i+1] = item_to_check


letters = ['b', 'c', 'k', 'a', 'z', 'n', 'j', 's']
shifting(letters, 3)
print(letters)
