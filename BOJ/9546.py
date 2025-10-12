T = int(input())

for _ in range(T):
    k = int(input())

    print(sum([2**i for i in range(k)]))