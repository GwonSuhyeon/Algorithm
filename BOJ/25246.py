s = input()

arr = set(['a', 'e', 'i', 'o', 'u'])

for idx, i in enumerate(s[::-1]):
    if i in arr:
        s = s[:len(s) - idx]
        break

print(s + 'ntry')