import sys


line = list(map(int, sys.stdin.read().replace('\n', '').split(',')))

print(sum(line))