def get_first_n_fibonacci_numbers(n):
    if n == 1 or n == 2:
        return 1
    fibo_arr = [1, 1]
    a, b = 1, 1
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
        fibo_arr.append(b)
    return fibo_arr
