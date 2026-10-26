# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

# Find and print min and max
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
