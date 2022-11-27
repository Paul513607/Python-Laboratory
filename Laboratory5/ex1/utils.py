import math


def is_prime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


def process_item(x):
    was_found = False
    next_num = x + 1 if x % 2 == 0 else x + 2
    while not was_found:
        was_found = is_prime(next_num)
        next_num += 2
    return next_num - 2
