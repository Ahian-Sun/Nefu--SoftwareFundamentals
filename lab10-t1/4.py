# coding: utf-8
# Ahian


def get_first_mid_last(words_list):
    for i in range(len(words_list)):
        if len(words_list[i]) >= 3:
            words_list[i] = words_list[i][0] + words_list[i][len(words_list[i])//2] + words_list[i][-1]
    return words_list


list1 = ["Japan", "America"]
print(get_first_mid_last(list1))
print(get_first_mid_last(["Hello", "World", "is", "nice", "weather"]))