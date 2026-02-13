total = 0

while True:
    number = int(input("Enter a number: "))
    
    if number == 0:
        break   # Stop when 0 is entered
    
    total += number

print("Total:", total)
