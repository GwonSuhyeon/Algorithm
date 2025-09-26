N = int(input())
X = int(input())

res = 0

for _ in range(N):
    P1, P2 = map(int, input().split())

    if abs(P1 - P2) <= X:
        res += max(P1, P2)
    else:
        res += int(input())

print(res)