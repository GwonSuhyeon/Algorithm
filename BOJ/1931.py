import sys


input = sys.stdin.readline

N = int(input().rstrip())

times = []

for _ in range(N):
    start, end = map(int, input().rstrip().split())
    
    times.append([start, end])

times = sorted(times, key=lambda x: (x[1], x[0]))

time_sum = 0
res = 0

for start, end in times:
    if start < time_sum:
        continue
    
    time_sum = end
    res += 1

print(res)