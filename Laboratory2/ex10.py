def make_tuples(*lists):
    max_len = max([len(list_el) for list_el in lists])
    for list_el in lists:
        while len(list_el) < max_len:
            list_el.append(None)
    return list(zip(*lists))
