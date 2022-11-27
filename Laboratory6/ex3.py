import re


def get_substrings_matching_at_least_one_regex(text, *regex_list):
    matches = []
    for regex in regex_list:
        if re.search(regex, text):
            matches.extend(re.findall(regex, text))
    return matches
