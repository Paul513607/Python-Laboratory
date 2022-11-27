def get_numbers(my_list):
    return [item for item in my_list if type(item) in {int, float}]