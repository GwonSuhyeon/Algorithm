import sys


N = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

res = ''

for i in range(N - 1):
    for k in range(i + 1, N):
        num1 = int(str(arr[i]) + str(arr[k]))
        num2 = int(str(arr[k]) + str(arr[i]))
        
        if num1 < num2:
            temp = arr[i]
            arr[i] = arr[k]
            arr[k] = temp

for i in arr:
    res += str(i)

res = int(res)

if res == 0:
    print(0)

else:
    print(res)