string = "Hello"

# 1. Third character
if len(string) >= 3:
    print(string[2])

# 2. Penultimate character
if len(string) >= 2:
    print(string[-2])

# 3. First five characters
print(string[:5])

# 4. All except the last two characters
print(string[:-2])

# 5. All characters with even indices
print(string[::2])

# 6. All characters with odd indices
print(string[1::2])

# 7. All characters in reverse order
print(string[::-1])

# 8. Every other character in reverse order
print(string[::-2])

# 9. Length of the string
print(len(string))