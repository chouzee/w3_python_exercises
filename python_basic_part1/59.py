def height_convert(value):
    feet = value * 30.48
    inches = value * 2.54
    return feet, inches

print(height_convert(30))
