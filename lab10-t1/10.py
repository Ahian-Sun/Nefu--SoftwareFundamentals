# coding: utf-8
# Ahian
def weighted_binary_search(data, value):
    low_indices = 0
    high_indices = len(data) - 1
    m_index = 0
    while low_indices < high_indices and data[m_index] != value:
        m_index = int((value-data[low_indices])/(data[high_indices] - data[low_indices]) * (high_indices - low_indices) + low_indices)
        if data[m_index] == value:
            break
        print("Searching mid index: {}".format(m_index))
        low_indices = m_index + 1
        if low_indices > high_indices:
            return -1
            break
        if data[0] > value:
            return -1
            break
        if data[low_indices] > value:
            print("Searching mid index: {}".format(m_index))
            return -1
            break
    print("Searching mid index: {}".format(m_index))
    return m_index

print(weighted_binary_search([1, 2, 4, 5], -4))