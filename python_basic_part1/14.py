from datetime import date

d1 = date(2014, 7, 11)
d2 = date(2014, 7, 2)

delta = d1 - d2
print(delta.days)
