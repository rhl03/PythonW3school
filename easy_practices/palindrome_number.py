n = int(input())

# Check if n is a palindrome using arithmetic (no string conversion)
input = n
digit: int = 0

while n > 0:
    digit = digit * 10 + n % 10
    n //= 10

if input == digit:
    print("Yes")
else:
    print("No")
