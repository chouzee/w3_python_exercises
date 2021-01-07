user_string = 'The quick brown fox jumps over the lazy dog.'

for i in user_string:
    if i not in "a,e,i,o,u":
        print(i, end="")
