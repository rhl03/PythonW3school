# Read input
first_name = input().strip()
last_name = input().strip()

# Create username (lowercase, no space)
first = first_name.lower()
last = last_name.lower()
username = first + last
# Create initials (uppercase first letters)
firstletter = first_name[0]
lastletter = last_name[0]
initials = firstletter + lastletter
# Print results
print(f"Username: {username}")
print(f"Initials: {initials}")
