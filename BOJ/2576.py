arr = []

for _ in range(7):
    arr.append(int(input()))

odd = []

for i in arr:
    if i % 2 != 0:
        odd.append(i)

if odd:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)