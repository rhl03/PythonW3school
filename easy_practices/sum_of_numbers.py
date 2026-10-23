# Read count
n = int(input())

# Read numbers and calculate sum
total = 0
for i in range(1, n + 1):
    numbers = int(input())
    total = numbers + total
# Print the sum
print(f"Sum: {total}")
