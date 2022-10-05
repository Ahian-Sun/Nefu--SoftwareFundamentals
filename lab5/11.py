# coding: utf-8
# Ahian


def read_scores(filename):
    try:
        if type(filename) == str and len(filename) == 0:
            raise ValueError("ERROR: Invalid filename!")
        elif type(filename) != str:
            raise ValueError("ERROR: Invalid input!")
        input_file = open(filename, "r")
        scores = input_file.read().split()
        try:
            numbers = [float(score) for score in scores if float(score) >= 0 ]
        except:
            raise ValueError("ERROR: The input file contains invalid values.")
        if len(numbers) == 0:
            raise ValueError('ERROR: No positive scores in the input file.')
            input_file.close()
        elif len(numbers) != 0:
            number_of_marks = len(numbers)
            total_marks = sum(numbers)
            print("There are {} score(s).".format(number_of_marks))
            print("The total is {:.2f}.".format(total_marks))
            print("The average is {:.2f}.".format(total_marks/number_of_marks))
            input_file.close()
    except FileNotFoundError:
        print("ERROR: The file '{}' does not exist.".format(filename))
    except ValueError as err:
        print(err)


