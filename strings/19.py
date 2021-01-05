def get_last_part(delim, arg):
    return (arg.rsplit(delim, 1)[0])


print(get_last_part("/", "https://www.w3resource.com/python-exercises/string"))
print(get_last_part("-", "https://www.w3resource.com/python-exercises/string"))
