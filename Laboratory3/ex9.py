def intersect(a, b):
    if type(a) == tuple and type(b) == dict:
        return [x for x in a if x in b.values()]
    return a & b


def my_function(*positional_args, **keyword_args):
    return len(intersect(positional_args, keyword_args))
