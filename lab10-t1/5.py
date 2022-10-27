# coding: utf-8
# Ahian


def generate_words(filename):
    try:
        if filename == "":
            raise ValueError("ERROR: Invalid filename!")
        with open(filename) as f:
            f = f.read()
            lis = f.split()
            lis1 = []
            for i in range(len(lis)):
                if len(lis[i]) >= 3:
                    lis[i] = lis[i][0] + lis[i][len(lis[i])//2] + lis[i][-1]
                    if lis[i].lower() not in lis1:
                        lis1.append(lis[i].lower())
    except ValueError as a:
        return a
    except FileNotFoundError:
        return "ERROR: The file '{}' does not exist.".format(filename)
    else:
        return lis1


