# coding: utf-8
# Ahian

def move_zero(list):
    left = 0
    right = 1
    while right < len(list):
        if list[left] == 0 and list[right] == 0:
            right += 1
        elif list[left] == 0 and list[right] != 0:
            list[left] = list[right]
            list[right] = 0
            left += 1
            right += 1
        elif list[left] != 0:
            left += 1
            right += 1
    return list
nums = [1,0]
print(move_zero(nums))


