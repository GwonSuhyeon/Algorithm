n = int(input())

for _ in range(n):
    num = int(input())

    res = 0

    for i in range(1, num + 1):
        res += (i * (i + 1)) // 2
    
    print(res)