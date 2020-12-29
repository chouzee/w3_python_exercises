def sum_of_three(f, s, t):
    summ = f + s + t
    if f == s == t:
        summ = summ * 3
    return summ
print(sum_of_three(10, 2, 7))
print(sum_of_three(10, 10, 10))
