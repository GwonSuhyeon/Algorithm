n = int(input())
arr = list(map(int, input().split()))

res = 0

for i in arr:
    if i == (res + 1):
        res += 1

print(n - res)