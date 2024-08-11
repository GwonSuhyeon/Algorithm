N = int(input())

arr = []

for _ in range(N):
    arr.append(input())

K = int(input())

if K == 1:
    for i in arr:
        print(i)
elif K == 2:
    for i in arr:
        print(i[::-1])
elif K == 3:
    for i in arr[::-1]:
        print(i)