N = int(input())

arr = []

for _ in range(N):
    arr.append(int(input()))

height_avg = sum(arr) // len(arr)

res = 0

for i in arr:
    if i > height_avg:
        res += (i - height_avg)

print(res)