def get_last_part(delim, arg):
    """ a little bit of note for myself....
    1. we do split by right side and cut 
    sentence by 2 parts, and leave a part after
    delimiter, then we are printing only that
    part, before delimiter. So,
    (delim, 1) - will print 2 parts inside a list,
    and by [0] we are printing part before delimiter. :)
    """
    return (arg.rsplit(delim, 1)[0])


print(get_last_part("/", "https://www.w3resource.com/python-exercises/string"))
print(get_last_part("-", "https://www.w3resource.com/python-exercises/string"))
