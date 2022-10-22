# coding: utf-8
# Ahian



def reverse_string(word):
    if len(word) > 1:
        print(word[-1], end='')
        reverse_string(word[:len(word)-1])
    return word[0]
s = 'hello'
print(reverse_string(s))
