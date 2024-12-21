T = int(input())

res = []

for _ in range(T):
    n, c = input().split()

    n = int(n)
    c = ord(c) - ord('A')

    lines = []

    for i in range(n):
        lines.append((chr((c + i) % 26 + ord('A')) * (i + 1)))
    
    res.append(lines)

for i in res:
    for k in i:
        print(k)
    print()