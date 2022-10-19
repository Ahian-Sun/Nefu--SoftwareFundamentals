# coding: utf-8
# Ahian


def insertion_row(data, index):
    item_to_insert = data[index]
    i = index - 1
    while  i>= 0 and data[i] > item_to_insert:
        data[i+1] = data[i]
        i -= 1
        data[i+1] = item_to_insert

def my_insertion_sort(data):
    for i in range(len(data)):
        insertion_row(data,i)

letters = ['x', 'b', 'f', 'u', 'r', 'k']
my_insertion_sort(letters)
print(letters)

letters = ['h', 't', 'w', 'e', 'q', 'c', 'x']
insertion_row(letters, 3)
print(letters)