import sys


input = sys.stdin.readline

while True:
    N = int(input().rstrip())
    
    if N == 0:
        break
    
    if N == 1:
        print(0)
        
        continue
    
    res = N
    
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            while (N % i) == 0:
                N /= i
            
            res *= (1 - (1 / i))
    
    if N != 1:
        res *= (1 - (1 / N))
    
    print(int(res))