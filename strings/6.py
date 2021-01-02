def add_ing(s0):
    if len(s0) >= 3:
        if s0[-3:] == "ing":
            s0 += "ly"
        else:
            s0 += "ing"
    return s0
    
print(add_ing("abcing"))
print(add_ing("abc"))
print(add_ing("ab"))
