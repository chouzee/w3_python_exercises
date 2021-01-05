def uniq_sorted_words(words):
    words = words.split(",")
    print(",".join(sorted(list(set(words)))))
    
    
words = "red, white, black, red, green, black"
uniq_sorted_words(words)
