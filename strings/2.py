sample_string = "google.com"
sample_dict = {}
for k in sample_string:
    if k in sample_dict:
        sample_dict[k] += 1
    else:
        sample_dict[k] = 1
    
        
print(sample_dict)
