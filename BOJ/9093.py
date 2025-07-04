T = int(input())

for _ in range(T):
    line = input().split()
    
    for word in line:
        print(word[::-1], end=' ')