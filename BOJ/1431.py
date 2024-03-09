N = int(input())

arr = []

for _ in range(N):
    arr.append(input())

res = sorted(arr, key=lambda x : (len(x), sum([int(i) for i in x if i.isdigit()]), x))

for i in res:
    print(i)