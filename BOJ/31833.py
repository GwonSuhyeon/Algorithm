import sys

input = sys.stdin.readline

N = int(input().rstrip())

A = int(''.join(input().rstrip().split()))

B = int(''.join(input().rstrip().split()))

if A == B:
    print(A)

else:
    print(min(A, B))