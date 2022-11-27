import ex2, ex3, ex4, ex5, ex6, ex7, ex8, ex9


def sum_digits(x):
    return sum(map(int, str(x)))


def multiply_by_two(x):
    return x * 2


def add_numbers(a, b):
    return a + b


def multiply_by_three(x):
    return x * 3


if __name__ == '__main__':
    print("ex2: ", ex2.my_function(1, 2, c=3, d=4))
    print("ex2: ", ex2.my_function_lambda(1, 2, c=3, d=4))
    print("\nex3: ", ex3.get_all_vowels("Programming in Python is fun"))
    print("ex3: ", ex3.get_all_vowels_lambda("Programming in Python is fun"))
    print("ex3: ", ex3.get_all_vowels_list_comprehension("Programming in Python is fun"))
    print("ex3: ", ex3.get_all_vowels_with_filter("Programming in Python is fun"))
    print("\nex4: ", ex4.my_function({1: 2, 3: 4, 5: 6},
                                     {'a': 5, 'b': 7, 'c': 'e'},
                                     {2: 3},
                                     [1, 2, 3],
                                     {'abc': 4, 'def': 5},
                                     3764,
                                     dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
                                     test={1: 1, 'test': True}))
    print("\nex5: ", ex5.get_numbers([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
    print("\nex6: ", ex6.pair_evens_and_odds([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))
    print("\nex7: ",
          ex7.process(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
                      limit=2,
                      offset=2))
    print("\nex8:")
    print("Part 1:")
    augmented_multiply_by_two = ex8.print_arguments(multiply_by_two)
    x1 = augmented_multiply_by_two(10)  # this will print: Arguments are: (10,), {} and will return 20.
    print("\tOutput: ", x1)
    augmented_add_numbers = ex8.print_arguments(add_numbers)
    x1 = augmented_add_numbers(3, 4)  # this will print: Arguments are: (3, 4), {} and will return 7.
    print("\tOutput: ", x1)
    print("Part 2:")
    augmented_multiply_by_three = ex8.multiply_output(multiply_by_three)
    x1 = augmented_multiply_by_three(10)  # this will return 2 * (10 * 3)
    print("\tOutput: ", x1)
    print("Part 3:")
    decorated_function = ex8.augment_function(add_numbers, [ex8.print_arguments, ex8.multiply_output])
    x1 = decorated_function(3, 4)  # this will print: Arguments are: (3, 4), {} and will return (2 * (3 + 4))
    print("\tOutput: ", x1)
    print("\nex9: ", ex9.get_operations([(5, 2), (19, 1), (30, 6), (2, 2)]))
