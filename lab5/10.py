# coding: utf-8
# Ahian


phones_dictionary = {'Martin':8202, 'Angela':6620, 'Ann':4947, 'Damir':2391, 'Adriana':7113, 'Andrew':5654}
def get_phone(phones_dictionary, name):
    try:
        if name in phones_dictionary:
            return phones_dictionary[name]
        elif type(name) == str and name not in phones_dictionary and len(name) != 0:
            raise KeyError()
        elif type(name) == str and len(name) == 0:
            raise ValueError('ERROR: Invalid name!')
        else:
            raise ValueError("ERROR: Invalid input!")
    except KeyError  as err:
        return ("ERROR: {} is not available.".format(name))
    except ValueError as a:
        return a


print(get_phone(phones_dictionary , 'Ann'))
print(get_phone(phones_dictionary , 'Daniel'))
print(get_phone(phones_dictionary , 123))
print(get_phone(phones_dictionary , ''))
