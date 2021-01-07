def first_non_repeating_character(s):
    chars = []
    c = {}
    for char in s:
        if char in c:
            c[char] += 1
        else:
            c[char] = 1
            chars.append(char)
    for char in chars:
        if c[char] > 1:
            return char
    return None
    #print(c)


print(first_non_repeating_character('abcdef'))
print(first_non_repeating_character('abcabcdef'))
print(first_non_repeating_character('aabbcc'))
