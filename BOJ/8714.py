n = int(input())
arr = list(map(int, input().split()))

print(min(n - sum(arr), sum(arr)))