import sys


N = int(sys.stdin.readline().rstrip())

arr = sorted(set(map(int, sys.stdin.readline().rstrip().split())))

for i in arr:
    print(i, end=' ')