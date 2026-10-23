# Read count
n = int(input())

# Read scores and calculate average
total = 0
for i in range(1, n + 1):
    numbers = int(input())
    total = numbers + total
# Print the average
print(f"Average: {total / n:.1f}")
