# Employee Role Checker

# Store employee details as a tuple
employee = (101, "Arjun", "IT")

# Store employee roles in a set
roles = {"editor", "viewer", "admin"}

# Print employee information using tuple indexing
print("Employee Information")
print("ID:", employee[0])
print("Name:", employee[1])
print("Department:", employee[2])

# Check if 'admin' role exists
if "admin" in roles:
    print("Admin Access: Yes")
else:
    print("Admin Access: No")
