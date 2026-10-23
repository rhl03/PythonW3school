# Read input
price = float(input())
discount_percent = int(input())

# Calculate discount and final price
discount = price * discount_percent / 100
final = price - discount
# Print results
print(f"Discount: {discount:.2f}")
print(f"Final price: {final:.2f}")
