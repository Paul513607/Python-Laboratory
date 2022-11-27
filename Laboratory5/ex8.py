def print_arguments(function):
    def new_func(*args, **kwargs):
        print(f"\tArguments are: {args}, {kwargs}")
        return function(*args, **kwargs)
    return new_func


def multiply_output(function):
    return lambda *args, **kwargs: function(*args, **kwargs) * 2


def augment_function(function, decorators):
    for decorator in decorators:
        function = decorator(function)
    return function
