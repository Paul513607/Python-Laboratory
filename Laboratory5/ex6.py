def pair_evens_and_odds(my_list):
    evens = [num for num in my_list if num % 2 == 0]
    odds = [num for num in my_list if num % 2 == 1]
    return list(zip(evens, odds))
