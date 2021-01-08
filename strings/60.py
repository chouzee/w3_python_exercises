def capitalize_first_last_char(s):
    s = result = s.title()
    result = ""
    for word in s.split():
        result += word[:-1] + word[-1].upper() + " "
    return result[:-1]



print(capitalize_first_last_char("hello"))
