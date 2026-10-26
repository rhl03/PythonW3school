n = int(input())

# Calculate the sum of digits
digit_sum = 0
while n > 0:
    digit_sum = digit_sum + n % 10
    n = n // 10

print(digit_sum)
