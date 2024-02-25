import sys

n, m = map(int, input().split())

arr1 = []
arr2 = []

for _ in range(n):
    arr1.append(sys.stdin.readline().split('\n')[0])

for _ in range(m):
    arr2.append(sys.stdin.readline().split('\n')[0])

arr1 = set(arr1)
arr2 = set(arr2)

res = sorted(arr1.intersection(arr2))

print(len(res))

for i in res:
    print(i)