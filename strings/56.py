def find_first_repeated_word(s):
    d = {}
    for word in s.split():
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
            
    count = sorted(d.items(), key=lambda k: k[1])
    return count[-2]


print(find_first_repeated_word('tBoth of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expressions in annotations at their definition time, the compiler stores the annotation in a string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at runtime using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper to store (since short strings are interned by the interpreter) and make startup time faster."'))
