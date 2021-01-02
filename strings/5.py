def str_combine(s0, s1):
    s_0 = s1[:2] + s0[2:]
    s_1 = s0[:2] + s1[2:]
    print( s_0 + " " + s_1)
    
str_combine("abc", "xyz")
