import sys


N = int(sys.stdin.readline().rstrip())

A = 0
B = 0

for _ in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    if a > b:
        A += 1
    elif a < b:
        B += 1

print(A, B)