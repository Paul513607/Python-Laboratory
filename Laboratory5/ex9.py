import math


def get_operations(pairs):
    return [{'sum': pair[0] + pair[1], 'prod': pair[0] * pair[1], 'pow': int(math.pow(pair[0], pair[1]))} for pair in pairs]