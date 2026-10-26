sentence = input().strip()
words = sentence.split()

# Capitalize the first letter of each word
capitalized: list[str] = [word[0].upper() + word[1:] for word in words]

print(" ".join(capitalized))
