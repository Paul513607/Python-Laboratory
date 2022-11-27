def operate_on_sets(*sets):
    my_dict = {}
    for i in range(0, len(sets) - 1):
        for j in range(i + 1, len(sets)):
            my_dict[f"{sets[i]} | {sets[j]}"] = sets[i] | sets[j]
            my_dict[f"{sets[i]} & {sets[j]}"] = sets[i] & sets[j]
            my_dict[f"{sets[i]} - {sets[j]}"] = sets[i] - sets[j]
            my_dict[f"{sets[j]} - {sets[i]}"] = sets[j] - sets[i]
    return my_dict
