s = "python"
new_s = ""
for item in range(len(s)):
    if item % 2 == 0:
        new_s = new_s + s[item]

print(new_s)
