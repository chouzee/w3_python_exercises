def find_first_repeated_word(s):
    d = set()
    for word in s.split():
        if word in d:
            return word
        else:
            d.add(word)
    return 'None'
        


print(find_first_repeated_word('the big little guy'))
print(find_first_repeated_word('the one that the other'))
