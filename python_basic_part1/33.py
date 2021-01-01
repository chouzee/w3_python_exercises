def sum_three_digits(n0, n1, n2):
    """
    If one two of three digits are equal
    the sum have to be 0
    """
    if n0 == n1 or n1 == n2 or n0 == n2:
        return 0
    else:
        return n0+n1+n2


print(sum_three_digits(10, 10, 20))
