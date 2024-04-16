import sys


input = sys.stdin.readline


def back_tracking():
    if len(disit) == N:
        res.append(disit.copy())
        
        return
    
    for i in range(1, N + 1):
        if i in disit:
            continue
        
        disit.append(i)
        
        back_tracking()
        
        disit.pop()
        
N = int(input().rstrip())

disit = []
res = []

back_tracking()

for i in res:
    for k in i:
        print(k, end=' ')
    print()