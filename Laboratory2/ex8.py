def get_specific_chars(strings, x=1, flag=True):
    if strings is None:
        strings = []
    result = []
    for string in strings:
        string_result = [char for char in string if flag and ord(char) % x == 0 or not flag and ord(char) % x != 0]
        result.append(string_result)
    return result
