L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

k, m = 0, 0

if A % C == 0:
    k = A // C
else:
    k = (A // C) + 1

if B % D == 0:
    m = B // D
else:
    m = (B // D) + 1

L -= max(k, m)

print(L)