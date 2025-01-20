T = int(input())

for _ in range(T):
    arr = list(map(int, input().split()))

    temp = []

    for i in arr:
        if i % 2 == 0:
            temp.append(i)
    
    print(f'{sum(temp)} {min(temp)}')