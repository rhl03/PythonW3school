# Read N
n = int(input())

# Calculate and print the sum
total = 0
for i in range(1, n + 1):
    total = i + total
# Print the sum
print(f"Sum: {total}")
