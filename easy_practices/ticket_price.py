# Read age from input
age = int(input())

# Determine ticket type and price based on age
if age <= 11:
    type = "Child"
    price = 5
elif 12 <= age <= 64:
    type = "Adult"
    price = 15
else:
    type = "Senior"
    price = 8
# Print results
print(type)
print(f"${price}")
