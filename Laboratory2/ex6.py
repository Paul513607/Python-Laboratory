def get_items_that_apprear_x_times(*lists, x):
    dict = {}
    for list in lists:
        for item in list:
            if item in dict:
                dict[item] += 1
            else:
                dict[item] = 1
    return [key for key in dict.keys() if dict.get(key) == x]
