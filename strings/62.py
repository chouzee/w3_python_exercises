def compute_digits_sum(s):
    summ = 0
    for i in s:
        if i.isdigit():
            i = int(i)
            summ += i
    return summ
    

print(compute_digits_sum("1hello3"))
print(compute_digits_sum("12H1E13ll1"))
