def count_occurences(sentence, word):
    return sentence.count(word)


sentence = "Today I learned today which I Today"
print(count_occurences(sentence, "Today"))


def word_count(words):
    word_dict = {}
    words = words.split()
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict


print(word_count("the quick brown fox jumps over the lazy dog."))
