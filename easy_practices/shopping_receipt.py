# Read input
item = input().strip()
price = float(input())
quantity = int(input())

# Calculate total
total = price * quantity
# Print the receipt
print(f"Item: {item}")
print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: ${total:.2f}")
