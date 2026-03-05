N = int(input())

res = ''
maximum = 0

for _ in range(N):
    name = input()
    bid = int(input())

    if bid > maximum:
        maximum = bid
        res = name

print(res)