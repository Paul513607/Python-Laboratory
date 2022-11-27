def compare_dicts(dict1, dict2, result, number_of_tabs=0):
    tabs = ""
    for i in range(0, number_of_tabs):
        tabs += '\t'
    if len(dict1) != len(dict2):
        result.append(f"{tabs}[Dictionary] Different lengths")
    for key, val in dict1.items():
        if key not in dict2.keys():
            result.append(f"{tabs}[Dictionary] Key {key} not found in dictionary 2")
        else:
            val2 = dict2.get(key)
            if type(val) != type(val2):
                result.append(f"{tabs}[Type] Types differ for values for key {key}")
            else:
                # Primitive types
                if type(val) in {int, float, chr, str}:
                    if val != val2:
                        result.append(f"{tabs}[Primitive] Values differ for key {key}")
                # Lists, Tuples
                elif type(val) in {list, tuple}:
                    next_result = compare_lists(val, val2, [], number_of_tabs + 1)
                    if len(next_result) > 0:
                        result.append(f"{tabs}[List/Tuple] Differences on value for key {key}:")
                        result.append(next_result)
                # Set
                elif type(val) in {set}:
                    next_result = compare_sets(val, val2, [], number_of_tabs + 1)
                    if len(next_result) > 0:
                        result.append(f"{tabs}[Set] Differences between sets:")
                        result.append(next_result)
                # Dictionaries
                elif type(val) is dict:
                    next_result = compare_dicts(val, val2, [], number_of_tabs + 1)
                    if len(next_result) > 0:
                        result.append(f"{tabs}[Dictionary] Differences on value for key {key}:")
                        result.append(next_result)
    return result


def compare_lists(list1, list2, result, number_of_tabs):
    tabs = ""
    for i in range(0, number_of_tabs):
        tabs += '\t'
    if len(list1) != len(list2):
        result.append(f"{tabs}[List/Tuple] Different lengths")
    for index in range(0, len(list1)):
        # Type
        if type(list1[index]) != type(list2[index]):
            result.append(f"{tabs}[Type] Different types for index {index}")
        # Primitive
        if type(list1[index]) in {int, float, chr, str} and list1[index] != list2[index]:
            result.append(f"{tabs}[Primitive] Values differ for index {index}")
        # List/Tuple
        elif type(list1[index]) in {list, tuple}:
            next_result = compare_lists(list1[index], list2[index], [], number_of_tabs + 1)
            if len(next_result) > 0:
                result.append(f"{tabs}[List/Tuple] Differences on index {index}:")
                result.append(next_result)
        # Set
        elif type(list1[index]) in {set}:
            next_result = compare_sets(list1[index], list2[index], [], number_of_tabs + 1)
            if len(next_result) > 0:
                result.append(f"{tabs}[Set] Differences on index {index}:")
                result.append(next_result)
        # Dictionaries
        elif type(list1[index]) is dict:
            next_result = compare_dicts(list1[index], list2[index], [], number_of_tabs + 1)
            if len(next_result) > 0:
                result.append(f"{tabs}[Dictionary] Differences for index {index}:")
                result.append(next_result)
    return result


def compare_sets(set1, set2, result, number_of_tabs):
    tabs = ""
    for i in range(0, number_of_tabs):
        tabs += '\t'
    if len(set1) != len(set2):
        result.append(f"{tabs}[Set] Different lengths")
    for item1, item2 in zip(set1, set2):
        # Type
        if type(item1) != type(item2):
            result.append(f"{tabs}[Type] Different types")
        if type(item1) in {int, float, chr, str} and item1 != item2:
            result.append(f"{tabs}[Primitive] Values {item1}, {item2} differ")
        elif type(item1) in {list, tuple} and type(item2) in {list, tuple}:
            next_result = compare_lists(item1, item2, [], number_of_tabs + 1)
            if len(next_result) > 0:
                result.append(f"{tabs}[List/Tuple] Differences between lists/tuples:")
                result.append(next_result)
        # Set
        elif type(item1) in {set}:
            next_result = compare_sets(item1, item2, [], number_of_tabs + 1)
            if len(next_result) > 0:
                result.append(f"{tabs}[Set] Differences between sets:")
                result.append(next_result)
        # Dictionaries
        elif type(item1) is dict:
            next_result = compare_dicts(item1, item2, [], number_of_tabs + 1)
            if len(next_result) > 0:
                result.append(f"{tabs}[Dictionary] Differences between dicts:")
                result.append(next_result)
    return result


def print_result(result):
    for item in result:
        if type(item) is list:
            print_result(item)
        else:
            print(item)


def compare_dictionaries(dict1, dict2):
    result = []
    compare_dicts(dict1, dict2, result)
    print_result(result)
    return len(result) > 0
