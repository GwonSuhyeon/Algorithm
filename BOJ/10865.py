import sys


input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

relation = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().rstrip().split())

    relation[A].append(B)
    relation[B].append(A)

for i in range(1, N + 1):
    print(len(relation[i]))