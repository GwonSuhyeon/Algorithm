n  = int(input())
arr = list(map(int, input().split()))

res = 0
junk = 10**9 + 1

for idx, i in enumerate(arr):
    if i < junk:
        res = idx
        junk = i

print(res)