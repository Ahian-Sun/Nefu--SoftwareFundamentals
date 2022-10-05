# coding: utf-8
# Ahian

def set_list_element(a_list, index, value):
    try:
        a_list[index] = value
        if index > len(a_list):
            raise IndexError()
        elif type(index) != int:
            raise TypeError()
    except IndexError as err:
        print('ERROR: Invalid index:',str(index)+'.')
    except TypeError:
        print('ERROR: Invalid input.')

list1 = [1, 2, 3]
set_list_element(list1, 1, 10);
print(list1)
list1 = [1, 2, 3]
set_list_element (list1, 4, 10);
print(list1)
list1 = [1, 2, 3]
set_list_element(list1, 'two', 10);
print(list1)