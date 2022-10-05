# coding: utf-8
# Ahian

def count_consonants(word):
    list1 = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
    num = 0
    try:
        if type(word) == str:
            for i in word:
                if i.lower() in list1:
                    num += 1
            return num
        else:
            raise ValueError()
    except:
        return ("ERROR: Invalid input!")

print(count_consonants('abcdef'))

print(count_consonants('123'))

print(count_consonants(123))
print(count_consonants(''))

print(count_consonants([123]))