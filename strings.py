#6 find uncommon words in 2 strings
s1 = input("Enter first string: ").split()
s2 = input("Enter second string: ").split()

result = []

for word in s1:
    if word not in s2:
        result.append(word)

for word in s2:
    if word not in s1:
        result.append(word)

print("Uncommon words:", result)