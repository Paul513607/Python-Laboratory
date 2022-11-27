def intersect(a, b):
    if type(a) == type(b) == list:
        return [x for x in a if x in b]
    return a & b


def union(a, b):
    if type(a) == type(b) == list:
        return list(set(a + b))
    return a | b


def diff(a, b):
    if type(a) == type(b) == list:
        return [x for x in a if x not in b]
    return a - b


def set_operations(a, b):
    return [intersect(a, b), union(a, b), diff(a, b), diff(b, a)]
