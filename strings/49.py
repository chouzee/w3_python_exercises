s_string = "w3resource"

def count_vowels(text):
    letter_count = ""
    vowels = "aeiouAEIOU"
    for i in text:
        if i in vowels:
            letter_count += i
    print(letter_count)
    return len(letter_count)

print(count_vowels(s_string))
