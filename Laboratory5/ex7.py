def process(**args):
    fib = [0, 1]
    for i in range(2, 1000):
        fib.append(fib[i - 1] + fib[i - 2])
    if "filters" in args:
        fib = [x for x in fib if all([func(x) for func in args["filters"]])]
    if "offset" in args:
        fib = fib[args["offset"]:]
    if "limit" in args:
        fib = fib[:args["limit"]]
    return fib
