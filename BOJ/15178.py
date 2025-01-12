T = int(input())

for _ in range(T):
    a, b, c = map(int, input().split())

    if a + b + c == 180:
        print(f'{a} {b} {c} Seems OK')
    else:
        print(f'{a} {b} {c} Check')