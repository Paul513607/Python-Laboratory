def order_tuples(*tuples):
    return sorted(tuples, key=lambda tup: tup[1][2])
