def rm_index(word, n, char):
    r = word[:n] + char + word[n+1:]
    print(r)
rm_index("python", 4, "x")
