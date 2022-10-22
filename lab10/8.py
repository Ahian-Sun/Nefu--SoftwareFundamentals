# coding: utf-8
# Ahian


def get_max_len_list(words):
    if len(words) == 1:
        return len(words[0])
    elif len(words[0]) > len(words[1]):
        words[1] = words[0]
        return get_max_len_list(words[1:])
    elif len(words[0]) <= len(words[1]):
        return get_max_len_list(words[1:])

lst = ['This', 'is', 'a', 'test']
print(get_max_len_list(lst))

lst = ['hello']
print(get_max_len_list(lst))