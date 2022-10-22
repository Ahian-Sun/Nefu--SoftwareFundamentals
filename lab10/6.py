# coding: utf-8
# Ahian


def get_first_lower_case(word):
    if len(word) == 1 and "a" > word[-1] or word[-1] > "z":
        return None
    elif "a" <= word[0] <= "z":
        return word[0]
    else:
        return get_first_lower_case(word[1:])


s = 'WELL done'
print(get_first_lower_case(s))

s = 'GREAT'
print(get_first_lower_case(s))
