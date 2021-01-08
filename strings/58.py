def move_spaces(s):
    ch = []
    for c in s:
        if c != " ":
            ch.append(c)
    spaces_char = len(s) - len(ch)
    result = " "*spaces_char
    result = "'" + result + "".join(ch)+"'"
    return(result)



print(move_spaces("w3resource .  com  "))
print(move_spaces("   w3resource.com  "))
