L = int(input())

for _ in range(L):
    num, a = input().split()
    
    for _ in range(int(num)):
        print(a, end='')
    
    print()