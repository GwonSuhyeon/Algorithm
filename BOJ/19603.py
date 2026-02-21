P = int(input())
N = int(input())
R = int(input())

day = 0
total = N
r = 1

while True:
    day += 1

    r *= R
    total += (N * r)

    if total > P:
        break

print(day)