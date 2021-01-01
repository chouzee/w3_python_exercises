def add_objects(n0, n1):
    if (isinstance(n0, int) and isinstance(n1, int)):
        return n0 + n1
    else:
        return("One of the values is not an integer")
    
print(add_objects(2, 2.5))
