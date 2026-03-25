#15 remove vowels
s = input("Enter string: ")
print(''.join(c for c in s if c.lower() not in 'aeiou'))