import re


def get_matches_with_length_x(regex_string, text, x):
    regex = re.compile(regex_string)
    return [match for match in regex.findall(text) if len(match) == x]
