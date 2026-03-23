N = int(input())
arr = list(map(int, input().split()))

res = sum(arr) - max(arr) - min(arr)

print(res)