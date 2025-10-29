N = int(input())

arr = {}

for _ in range(N):
    title, score = input().split()

    arr[int(score)] = title

print(arr[min(arr.keys())])