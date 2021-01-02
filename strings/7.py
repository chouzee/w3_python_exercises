def test(sample_string):
    f = sample_string.find('not')
    f1 = sample_string.find('poor')

    if f1 > f and f > 0 and f1 > 0:
        sample_string = sample_string.replace(sample_string[f:(f1+4)], 'good')
        return sample_string
    else:
        return sample_string


print(test('The lyrics is not that poor!'))
print(test('The lyrics is poor!'))
