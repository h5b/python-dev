def exclusive(list_a, list_b):
    return list(set(list_a) ^ set(list_b))

def intersect(list_a, list_b):
    return list(set(list_a) & set(list_b))

def union(list_a, list_b):
    return list(set(list_a) | set(list_b))
