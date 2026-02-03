import math


n, s = map(int, input().split())
arr = list(map(int, input().split()))

print(math.ceil((s * max(arr)) / 1000))