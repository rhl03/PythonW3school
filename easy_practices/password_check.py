# Read the password
password = input().strip()

# Check length and print
check = len(password)
if check >= 8:
    print("Valid")
else:
    print("Invalid")
