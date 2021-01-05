def first_three(user_input):
    length = len(user_input)
    if length < 3:
        return user_input
    else:
        return user_input[:3]
    # I like the solution approach
    #return str[:3] if len(str) > 3 else str

print(first_three("ip"))
print(first_three("python"))
