def sort_lexicographically(s):
    return sorted(sorted(s), key=str.upper)


print(sort_lexicographically("w3resource"))
