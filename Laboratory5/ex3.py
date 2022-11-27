def get_all_vowels(string):
    vowels = 'aeiou'
    string_vowels = []
    for letter in string.lower():
        if letter in vowels:
            string_vowels.append(letter)
    return string_vowels


get_all_vowels_lambda = lambda string: [letter for letter in string.lower() if letter in 'aeiou']


def get_all_vowels_list_comprehension(string):
    return [letter for letter in string.lower() if letter in 'aeiou']


def get_all_vowels_with_filter(string):
    return list(filter(lambda letter: letter in 'aeiou', string.lower()))