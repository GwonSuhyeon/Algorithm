import sys
from collections import defaultdict


input = sys.stdin.readline

n = int(input().rstrip())

names = defaultdict(int)

for _ in range(n):
    name = input().rstrip()

    names[name] += 1

print(len([i for i in names.values() if i > 1]))