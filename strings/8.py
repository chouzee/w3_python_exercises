def return_longest(lst):
    word_len = []
    for item in lst:
        word_len.append((len(item), item))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]

lst = ["Exercises", "Hello", "Suspicious", "Simple"]
r = return_longest(lst)
print("The longest word is: " + r[1])
print("The length of longest word is: " + str(r[0]))
