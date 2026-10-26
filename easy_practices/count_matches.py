# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
target = int(input())

# Count and print
count = 0
for num in numbers:
    if num == target:
        count += 1

print(f"Count: {count}")
