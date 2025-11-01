N = input()[::-1]

res = []

for i in range(0, len(N), 3):
    if i + 3 >= len(N):
        res.append(N[i::][::-1])
    else:
        res.append(N[i:i+3][::-1])

print(','.join(res[::-1]))