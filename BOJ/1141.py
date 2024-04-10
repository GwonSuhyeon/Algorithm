import sys


N = int(sys.stdin.readline().rstrip())

arr = []

for _ in range(N):
    arr.append(sys.stdin.readline().rstrip())

arr = sorted(arr, reverse=True)

res = []

for i in arr:
    check = True
    
    for k in res:
        if i == k[:len(i)]:
            check = False
            
            break
    
    if check == True:
        res.append(i)

print(len(res))