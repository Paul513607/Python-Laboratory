def get_occurences(string):
    dictionary = {}
    for ch in string:
        dictionary[ch] = 1 if ch not in dictionary else dictionary[ch] + 1
    return dictionary
