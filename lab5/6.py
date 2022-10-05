# coding: utf-8
# Ahian

def get_sum_even(numbers):
    s = 0
    for i in numbers:
        try:
            if i % 2 == 0:
                 s = i +s
        except:
            pass
        continue
    return s


my_list = [1, 2, 3, 4, "two", 2]
print(get_sum_even(my_list))