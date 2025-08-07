T = int(input())

for _ in range(T):
    n = int(input())
    grades = list(map(int, input().split()))
    
    if abs(((min(grades) + max(grades)) / 2) -  (sum(grades) / len(grades))) < 1:
        print('Yes')
    else:
        print('No')