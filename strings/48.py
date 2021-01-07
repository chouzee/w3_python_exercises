s_string = "32.054,23"

trans = s_string.maketrans
s_string = s_string.translate(trans(",.", ".,"))
print(s_string)
