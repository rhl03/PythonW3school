import math

# Read radius
radius = float(input())

# Calculate and print
area = math.pi * radius * radius
circumference = 2 * math.pi * radius
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
