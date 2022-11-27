def loop(mapping):
    value = mapping["start"]
    visited = ["start"]
    while value in mapping and value not in visited:
        visited.append(value)
        value = mapping[value]
    return visited
