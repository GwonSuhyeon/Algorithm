import sys

N = int(input())
cards = {}
for idx, i in enumerate(map(int, sys.stdin.readline().rstrip().split())):
    cards[i] = idx

M = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

res = []

for i in arr:
    if i in cards:
        print(1, end=' ')
    
    else:
        print(0, end=' ')