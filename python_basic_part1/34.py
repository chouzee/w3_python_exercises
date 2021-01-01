def sum_two_numbers(n0, n1):
    """
    Return 20 if value between
    15 and 20
    """
    summ = n0+n1
    
    if summ >= 15 and summ <= 20:
        summ = 20
        return summ
    else:
        return summ
    
print(sum_two_numbers(10, 8))
