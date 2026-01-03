T = int(input())

for _ in range(T):
    A, B = input().split()

    if set(A) == set(B):
        print('YES')
    else:
        print('NO')