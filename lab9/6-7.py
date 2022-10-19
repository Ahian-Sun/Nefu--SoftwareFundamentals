# coding: utf-8
# Ahian


def get_position_of_highest(data, index):
    max_index = 0
    for i in range(index+1):
        if data[i] > data[max_index]:
            max_index = i
    return max_index

def selection_row(data, index):
    max_index = get_position_of_highest(data, index)
    max = data[max_index]
    data[max_index] = data[index]
    data[index] = max
    return data

def my_selection_sort(data):
    for i in range(len(data)-1,0,-1):
        selection_row(data,i)
    return data