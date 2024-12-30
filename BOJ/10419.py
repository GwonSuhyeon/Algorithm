T = int(input())

for _ in range(T):
    d = int(input())

    t = [i for i in range(d + 1) if (i**2) + i <= d]

    print(max(t))