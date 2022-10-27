# coding: utf-8
# Ahian


def modify_list(words_list):
    for i in range(1,len(words_list)+1):
        words_list[i-1] = words_list[i-1][i:]
    return words_list

data = ["1124310147@qq.", "com", "1234"]
modify_list(data)
print(data)


data = ["bushes", "and", "shrubs", "trees"]
modify_list(data)
print(data)
