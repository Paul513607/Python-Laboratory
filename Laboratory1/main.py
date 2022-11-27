def gcd_2(a, b):
    if a * b == 0:
        return 1
    if a == 0 or b == 0:
        return a + b
    while b:
        a, b = b, a % b
    return a


def gcd_2_recursive(a, b):
    if b == 0:
        if a == 0:
            return 1
        return a
    return gcd_2_recursive(b, a % b)


def gcd():
    args = []
    x = 1
    while x != 0:
        x = int(input("Enter numbers to find to find their gcd (0 to stop entering):"))
        if x != 0:
            args.append(x)
    print("args: ", args)
    if len(args) > 0:
        gcd_num = args[0]
        for i in range(1, len(args)):
            gcd_num = gcd_2(gcd_num, args[i])
        return gcd_num


def print_evens(args):
    print(list(filter(lambda x: x % 2 == 0, args)))


def count_vowels(string):
    count = 0
    vowels = 'aeiouAEIOU'
    for ch in string:
        if ch in vowels:
            count += 1
    return count


def count_occurrences_of_substring(substring, string):
    if len(substring) < len(string):
        substring, string = string, substring
    count = 0
    substring_len = len(substring)
    index = string.find(substring)
    while index != -1:
        count += 1
        index += substring_len
        index = string.find(substring, index)
    return count
    # or using prebuilt function
    # return string.count(substring)


def convert_pascal_to_snake_case(string):
    letters = list(string)
    new_letters = []
    if letters[0].isupper():
        new_letters.append(letters[0].lower())
    for index in range(1, len(letters)):
        if letters[index].isupper():
            new_letters.append('_')
        new_letters.append(letters[index].lower())
    return ''.join(new_letters)


def print_matrix_in_spiral(matrix):
    output = []

    i, j = 0, 0
    start_index, end_index = 0, len(matrix)
    count_marked = 0
    target = len(matrix) * len(matrix)
    while count_marked != target:
        for j in range(start_index, end_index):
            output.append(matrix[i][j])
            count_marked += 1
        for i in range(start_index + 1, end_index):
            output.append(matrix[i][j])
            count_marked += 1
        for j in range(end_index - 2, start_index - 1, -1):
            output.append(matrix[i][j])
            count_marked += 1
        for i in range(end_index - 2, start_index, -1):
            output.append(matrix[i][j])
            count_marked += 1
        start_index, end_index = start_index + 1, end_index - 1
        i = start_index

    print(''.join(output))


def is_palindrome(number):
    number_copy, ogl = number, 0
    while number_copy != 0:
        ogl = ogl * 10 + number_copy % 10
        number_copy //= 10
    return ogl == number


def find_ch_in_string(string, ch):
    for i in range(0, len(string)):
        if ch == string[i]:
            return i
    return -1


def extract_first_number(string):
    string = str(string)
    digits = "0123456789"
    min_index = len(string)
    for digit in digits:
        index = find_ch_in_string(string, digit)
        if index != -1 and index < min_index:
            min_index = index
    if min_index == len(string):
        return None

    result = []
    while string[min_index] in digits:
        result.append(string[min_index])
        min_index += 1
    return ''.join(result)


def count_number_of_bits_1(number):
    count = 0
    while number != 0:
        bit = number % 2
        number //= 2
        if bit == 1:
            count += 1
    return count


def get_most_common_letter(string):
    dict = {}
    string = string.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for ch in alphabet:
        dict[ch] = 0

    for letter in string:
        if letter in alphabet:
            dict[letter] += 1

    max_key = ''
    max_val = -1
    for (key, value) in dict.items():
        if value > max_val:
            max_key = key
            max_val = value
    return max_key


def get_number_of_words(text):
    count = 0
    text = text.strip()
    for index in range(0, len(text)):
        if text[index] == ' ' and text[index - 1] != ' ' and text[index + 1] != ' ':
            count += 1
    # add the first word
    return count + 1
    # or
    # return len(text.strip().split(' '))


if __name__ == '__main__':
    print(gcd())

    tmp_string = "ana are mere"
    print(f"Number of vowels in \"{tmp_string}\" is: {count_vowels(tmp_string)}")

    tmp_string1 = "egg"
    tmp_string2 = "this egg is egglicious, egg"
    print(f"Number of occurrences of \"{tmp_string1}\" in \"{tmp_string2}\" is: "
          f"{count_occurrences_of_substring(tmp_string1, tmp_string2)}")

    print(convert_pascal_to_snake_case("ThisIsACSharpCourse"))

    tmp_matrix = [['f', 'i', 'r', 's', 't'], ['b', '_', 'i', 's', '_'], ['a', 'e', '!', '_', 'p'],
                  ['l', 'r', 'e', 'h', 'y'], ['_', 'n', 'o', 'h', 't']]
    print_matrix_in_spiral(tmp_matrix)

    tmp_number1 = 123
    print(f"Is {tmp_number1} a palindrome? {is_palindrome(tmp_number1)}")
    tmp_number2 = 9669
    print(f"Is {tmp_number2} a palindrome? {is_palindrome(tmp_number2)}")

    tmp_string1 = "An apple is 123 USD"
    tmp_string2 = "abc123abc012"
    print(f"The first number in the string {tmp_string1} is: {extract_first_number(tmp_string1)}")
    print(f"The first number in the string {tmp_string2} is: {extract_first_number(tmp_string2)}")

    print("The number of bits of value 1 in the number 24 is:", count_number_of_bits_1(24))

    tmp_string = 'an apple is not a tomato'
    print(f"The most common letter in {tmp_string} is: {get_most_common_letter(tmp_string)}")

    tmp_string = 'I have Python exam'
    print(f"The number of words in the text {tmp_string} is: {get_number_of_words(tmp_string)}")

    print_evens([13, 0, 2, 15, 16, 22, 5, 16])

