s = input()
n = len(s)

res = 'Odd.'

for i in range(n - 1):
    if s[i] == s[i + 1]:
        res = 'Or not.'

        break

print(res)