balance = int(input("Balance: "))
withdrawal_amount = int(input("Withdrawal: "))

verified_input = input("Verified (True/False): ").strip().lower()

if verified_input == "true":
    is_verified = True
elif verified_input == "false":
    is_verified = False
else:
    print("Invalid verification status")
    exit()

if is_verified and withdrawal_amount <= balance:
    print("Withdrawal successful")
else:
    print("Transaction denied")
