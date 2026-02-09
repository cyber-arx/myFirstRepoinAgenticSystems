age = int(input("Age: "))

has_id_input = input("Has ID (True/False): ").strip().lower()

if has_id_input == "true":
    has_id = True
elif has_id_input == "false":
    has_id = False
else:
    print("Invalid input for ID status. Please enter True or False.")
    exit()

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
