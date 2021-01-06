def convert_to_upper(user_string):
    num_upper = 0
    for letter in user_string[:4]:
        if letter.upper() == letter:
            num_upper += 1
    if num_upper >= 2:
        return user_string.upper()
    return user_string
    
    
    
print(convert_to_upper("Python"))
print(convert_to_upper("PYthon"))
