CBP_a = list(map(int, input().split()))
CBP_r = list(map(int, input().split()))

res = 0

for a, r in zip(CBP_a, CBP_r):
    if r > a:
        res += (r - a)

print(res)