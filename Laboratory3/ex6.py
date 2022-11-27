def get_uniques_and_duplicates(my_list):
    my_set = set(my_list)
    return len(my_set), len(my_list) - len(my_set)