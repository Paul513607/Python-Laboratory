def intersect(a, b):
    intersection = []
    for item in a:
        if item in b:
            intersection.append(item)
    return [x for x in a for y in b if x == y]


def union(a, b):
    union_arr = a.copy()
    for item in b:
        if item not in union_arr:
            union_arr.append(item)
    return union_arr


def difference(a, b):
    return [x for x in a if x not in b]


def get_set_operations(a, b):
    return intersect(a, b), union(a, b), difference(a, b), difference(b, a)
