t = int(input())

for _ in range(t):
    line = input()

    ab = int(line[:2])
    cd = int(line[2:])

    if (ab**2 + cd**2) % 7 == 1:
        print('YES')
    else:
        print('NO')