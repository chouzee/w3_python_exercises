user_string = 'thequickbrownfoxjumpsoverthelazydog'
d = {}
for i in user_string:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
        
print(d)
