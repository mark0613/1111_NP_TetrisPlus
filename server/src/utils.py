import random
import string

LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits

def get_random_string(length: int=1):
    sequence = LOWER + UPPER + DIGITS
    result = ""
    if length < 1:
        length = 1
    for i in range(length):
        result += random.choice(sequence)
    return result
