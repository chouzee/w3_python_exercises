def find_first_repeated_char(s):
    d = {}
    for char in s:
        if char in d:
            return char, s.index(char)
        else:
            d[char] = 0
    return 'None'
        


print(find_first_repeated_char('abcabc'))
print(find_first_repeated_char('babbcc'))
