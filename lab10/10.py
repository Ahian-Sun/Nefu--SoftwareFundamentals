# coding: utf-8
# Ahian


def evaluate_m(i):
    if i == 1:
        return 1
    else:
        return evaluate_m(i-1) + 1/i

print('{} : {}'.format(2, evaluate_m(2)))
print('{} : {:.4}'.format(5, evaluate_m(5)))