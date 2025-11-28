N = int(input())
arr = list(map(int, input().split()))

res = min(arr) * max(arr)

print(res)