def is_group_member(data, n):
    for value in data:
        if n == value:
            return True
    return False

print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([1, 5, 8, 3], 2))
