def validate_dict(dictionary, *rules):
    for item in rules:
        key = item[0]
        if key not in dictionary:
            return False
        value = dictionary[key]
        index = value.find(item[1])
        if index != 0:
            return False
        length = len(item[2])
        index = value.find(item[2])
        if index == -1 or index == 0 or index == len(value) - length:
            return False
        length = len(item[3])
        index = value.find(item[3])
        if index != len(value) - length:
            return False
    return True
