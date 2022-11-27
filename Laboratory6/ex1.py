import re


def extract_words(text):
    word_regex = re.compile(r'[a-zA-z0-9]+')
    return word_regex.findall(text)
