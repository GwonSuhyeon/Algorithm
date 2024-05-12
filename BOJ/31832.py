import sys

input = sys.stdin.readline

N = int(input().rstrip())

for _ in range(N):
    name = input().rstrip()
    
    if len(name) > 10:
        continue
    
    try:
        temp = int(name)
        continue
    
    except Exception:
        small = 0
        large = 0
        
        for i in name:
            if 'a' <= i <= 'z':
                small += 1
            
            elif 'A' <= i <= 'Z':
                large += 1
        
        if small >= large:
            print(name)
            break