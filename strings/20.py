def reverse_string(s):
    if len(s) % 4 == 0:
        return s[::-1]
    else:
        return s


print(reverse_string("Ruby"))
print(reverse_string("Python"))
