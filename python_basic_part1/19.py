def is_strint(string):
    if string.startswith("Is"):
        return string
    else:
        return "Is " + string
    
    
print(is_strint("it possible?"))

# from solution section
def new_string(str):
  if len(str) >= 2 and str[:2] == "Is":
    return str
  return "Is" + str

print(new_string("Array"))
print(new_string("IsEmpty"))
