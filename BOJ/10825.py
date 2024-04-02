import sys


N = int(sys.stdin.readline().rstrip())

arr = []

for _ in range(N):
    temp = []
    s = sys.stdin.readline().rstrip().split()
    
    temp.append(s[0])
    temp.append(int(s[1]))
    temp.append(int(s[2]))
    temp.append(int(s[3]))
    
    arr.append(temp)

arr = sorted(arr, key=lambda x : (-x[1], x[2], -x[3], x[0]))

for i in arr:
    print(i[0])