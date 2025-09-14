T = int(input())

for _ in range(T):
    arr = input().split()

    res = float(arr[0])

    for i in arr[1:]:
        if i == '@':
            res *= 3
        elif i == '%':
            res += 5
        elif i == '#':
            res -= 7
    
    print(f'{res:.2f}')