# Ahian

def is_valid_score(score):
    try:
        if 0 <= score <= 100:
            return True
        if not 0 <= score <= 100:
            raise ValueError()
    except:
        return ("ERROR: Invalid score!")

print(is_valid_score(85.5))
print(is_valid_score(-1))
print(is_valid_score([16, 12]))
print(is_valid_score(123))
print(is_valid_score(0))
print(is_valid_score(100))
print(is_valid_score('sixteen'))