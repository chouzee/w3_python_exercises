def if_startswith(s, chars):
    if s.startswith(chars):
        return True
    else:
        return False


print(if_startswith("Hello", "H"))
print(if_startswith("World", "w"))
