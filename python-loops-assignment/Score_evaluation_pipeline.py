scores = [72, 45, 89, 30, 60]

for score in scores:
    if score < 50:
        print("Fail")
        continue   # Skip the rest of the loop for failed scores
    
    print("Pass")
