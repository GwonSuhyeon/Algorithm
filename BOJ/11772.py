N = int(input())

X = 0

for _ in range(N):
    P = input()

    X += int(P[:-1])**int(P[-1])

print(X)