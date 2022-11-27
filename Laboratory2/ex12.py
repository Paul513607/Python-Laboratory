def group_rhyming_words(words):
    dict = {}
    for word in words:
        last_2_chars = word[-2:]
        if last_2_chars not in dict:
            dict[last_2_chars] = [word]
        else:
            dict[last_2_chars].append(word)
    return list(dict.values())
