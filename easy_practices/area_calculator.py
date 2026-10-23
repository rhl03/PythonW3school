import math

# Read the shape
shape = input().strip()

# Read measurements and calculate area
if shape == "rectangle":
    width = float(input())
    height = float(input())
    print(f"Area: {width * height:.2f}")
elif shape == "triangle":
    base = float(input())
    height = float(input())
    area = base * height / 2
    print(f"Area: {area:.2f}")
else:
    radius = float(input())
    print(f"Area: {math.pi * radius * radius:.2f}")
