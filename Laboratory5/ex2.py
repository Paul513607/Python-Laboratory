def my_function(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


my_function_lambda = lambda *args, **kwargs: sum(args) + sum(kwargs.values())
