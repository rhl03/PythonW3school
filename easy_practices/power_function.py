def power(base: int, exp: int):
    result = 1
    # Calculate base^exp using a loop
    for i in range(exp):
        result = result * base
    return result


base = int(input())
exp = int(input())
print("Result: " + str(power(base, exp)))
