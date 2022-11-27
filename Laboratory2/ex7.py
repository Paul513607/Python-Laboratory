def is_palindrome(x):
    ogl, x_copy = 0, x
    while x_copy != 0:
        ogl = ogl * 10 + x_copy % 10
        x_copy //= 10
    return ogl == x


def is_palindrome_v2(x):
    # x_str = str(x)
    # x_str_reversed = x_str[::-1]
    # return x_str == x_str_reversed
    return str(x) == str(x)[::-1]


def get_number_and_greatest_of_palindromes(arr):
    palindromes = [x for x in arr if is_palindrome_v2(x)]
    return len(palindromes), max(palindromes)
