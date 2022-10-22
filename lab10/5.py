# coding: utf-8
# Ahian


f = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
def count_consonants(word):
    if len(word) > 0:
        if word[-1] in f:
            return count_consonants(word[:len(word)-1]) + 1
        else:
            return count_consonants(word[:len(word)-1]) + 0
    return 0

print(count_consonants('This is a Test'))
print(count_consonants('AEIOU'))
