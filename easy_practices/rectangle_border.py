# Read input
width = int(input())
height = int(input())

# Print the rectangle border
print("*" * width)
for i in range(height - 2):
    print("*" + " " * (width - 2) + "*")
print("*" * width)
