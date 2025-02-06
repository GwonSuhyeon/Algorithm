T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    res = 0

    if a == 1:
        res += 5000000
    elif 1 < a <= 3:
        res += 3000000
    elif 3 < a <= 6:
        res += 2000000
    elif 6 < a <= 10:
        res += 500000
    elif 10 < a <= 15:
        res += 300000
    elif 15 < a <= 21:
        res += 100000
    
    if b == 1:
        res += 5120000
    elif 1 < b <= 3:
        res += 2560000
    elif 3 < b <= 7:
        res += 1280000
    elif 7 < b <= 15:
        res += 640000
    elif 15 < b <= 31:
        res += 320000
    
    print(res)