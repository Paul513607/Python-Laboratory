import re


def censor_match(match):
    my_str = '*' * len(match.group(0))
    for idx in range(0, len(match.group(0)), 2):
        my_str = my_str[:idx] + match.group(0)[idx] + my_str[idx + 1:]
    return my_str


def censor_vowels_at_start_and_end_of_words(text):
    regex = re.compile(r'\b[aeiouAEIOU][a-zA-Z0-9]*[aeiouAEIOU]\b')
    return re.sub(regex, lambda match: censor_match(match), text)
