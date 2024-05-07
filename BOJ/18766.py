import sys


input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    res = False
    
    N = int(input().rstrip())
    
    arr1 = list(input().rstrip().split())
    arr2 = list(input().rstrip().split())
    
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    
    for a, b in zip(arr1, arr2):
        if a != b:
            res = True
            break
    
    if res == True:
        print('CHEATER')
    
    else:
        print('NOT CHEATER')