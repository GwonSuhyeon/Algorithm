T = int(input())

for t in range(T):
    L = int(input())

    a = input()
    b = input()

    res = 0

    for i, k in zip(a, b):
        if i != k:
            res += 1
    
    print(f'Case {t + 1}: {res}')