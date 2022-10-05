# coding: utf-8
# Ahian


dictionary ={'example': 'tauira', 'house': 'whare', 'apple': 'aporo', 'love': 'aroha', 'food': 'kai',
'hello': 'kiaora', 'work': 'mana', 'weather': 'huarere', 'greenstone': 'pounamu',
'red': 'whero', 'orange': 'karaka', 'black': 'mangu'}
def get_maori_word(dictionary, word):
    try:
        if word in dictionary:
            return dictionary[word]
        else:
            raise KeyError()
    except:
        return ('ERROR: {} is not available.'.format(word))

print(get_maori_word(dictionary, 'house'))

print(get_maori_word(dictionary, 'orange'))

print(get_maori_word(dictionary, 'tooth'))

