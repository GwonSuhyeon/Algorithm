import sys


def back_tracking(idx):
    
    temp = {'a', 'e', 'i', 'o', 'u'}
    
    if len(char) == L:
        if len(list(set(char) & temp)) >= 1 and len(list(set(char) - temp)) >= 2:            
            for i in char:
                print(i, end='')
            print()

        return
    
    for i in range(idx, C):
        char.append(arr[i])
        
        back_tracking(i + 1)
        
        char.pop()
    
L, C = map(int, sys.stdin.readline().rstrip().split())

arr = sys.stdin.readline().rstrip().split()
arr = sorted(arr)

char = []

back_tracking(0)