import sys


input = sys.stdin.readline

N = int(input().rstrip())

score = {}

for _ in range(N):
    A, B = input().rstrip().split()

    score[A] = int(B)

print(max(sorted(score), key=score.get))