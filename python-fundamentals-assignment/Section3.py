name = input("Enter your name: ")

age_input = input("Enter your age: ")
age = int(age_input)   # explicit type conversion

active_input = input("Are you an active user? (True/False): ")
is_active = active_input == "True"   # explicit conversion to boolean

print(f"User {name} is {age} years old. Active status: {is_active}")
