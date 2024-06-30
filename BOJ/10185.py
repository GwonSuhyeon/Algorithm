T = int(input())

for _ in range(T):
    p, q = map(int, input().split())
    
    print(f'f = {(float(p * q)/float(p + q)):.1f}')