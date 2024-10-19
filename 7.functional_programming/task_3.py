strings = ['abc', 'madam', 'racecar', 'hello', 'level']
palindromes = list(filter(lambda x: x == x[::-1], strings))
print(palindromes)
