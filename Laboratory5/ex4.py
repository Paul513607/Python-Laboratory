def check_requirements(item):
    if type(item) is not dict:
        return False
    if len(item) < 2:
        return False
    return any(list(map(lambda key: type(key) is str and len(key) >= 3, item.keys())))


def my_function(*args, **kwargs):
    return [item for item in args if check_requirements(item)] + [item for item in kwargs.values() if
                                                                  check_requirements(item)]
