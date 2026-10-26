s = input().strip()

# Reverse the string without using reversed() or [::-1]
char = list(s)
result1 = " "
result = ""

for i in char:
    last_char = char[-1]
    result1.join(last_char)
print(result)
