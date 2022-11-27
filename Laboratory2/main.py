import ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8, ex9, ex10, ex11, ex12

if __name__ == '__main__':
    print("ex1: First 10 fibonacci numbers: ", ex1.get_first_n_fibonacci_numbers(10))
    print()
    print("ex2: ", ex2.get_primes([1, 2, 5, 3, 16, 13, 18, 20, 17]))
    print()
    print("ex3: ", ex3.get_set_operations([1, 2, 3], [2, 3, 4, 5]))
    print()
    print("ex4: ", ex4.compose_song(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
    print()
    print("ex5: ", ex5.replace_matrix_values_under_main_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print()
    print("ex6: ", ex6.get_items_that_apprear_x_times([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"], x=2))
    print()
    print("ex7: ", ex7.get_number_and_greatest_of_palindromes([12, 151, 1668, 1521, 123321, 789987]))
    print()
    print("ex8: ", ex8.get_specific_chars(["test", "hello", "lab002"], 2, False))
    print("ex8: ", ex8.get_specific_chars(["test", "hello", "lab002"], 2))
    print()
    print("ex9: ", ex9.get_persons_that_can_not_see([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2],
                                            [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]]))
    print()
    print("ex10: ", ex10.make_tuples([1, 2, 3], [5, 6, 7], ["a", "b", "c"]))
    print()
    print("ex11: ", ex11.order_tuples(('abc', 'bcd'), ('abc', 'zza')))
    print()
    print("ex12: ", ex12.group_rhyming_words(['ana', 'banana', 'carte', 'arme', 'parte']))

