# coding: utf-8
# Ahian

def get_valid_input():
    number = -1
    while not 1 <= number <= 10:
        try:
            number = float(input("Enter a number between 1 and 10 inclusive: "))
            if 1 <= number <= 10:
                break
            else:
                raise ValueError()
        except:
            pass
    return float(number)
print("Valid input: {}".format(get_valid_input()))

