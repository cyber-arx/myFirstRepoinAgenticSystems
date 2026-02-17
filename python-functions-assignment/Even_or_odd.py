# Function definition
def check_even_odd(number):
    if number % 2 == 0:
        return "Number is Even"
    else:
        return "Number is Odd"

# Taking input from user
num = int(input("Enter a number: "))

# Function call
result = check_even_odd(num)

# Print result
print(result)
