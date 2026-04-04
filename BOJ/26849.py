import sys


input = sys.stdin.readline

N = int(input().rstrip())

res_min = (2 * 10**9) + 1
res_max = (1 / (2 * 10**9)) - 1
res_sum = 0

for _ in range(N):
    a, b = map(int, input().rstrip().split())

    value = a / b

    res_sum += value

    if value < res_min:
        res_min = value
    
    if value > res_max:
        res_max = value

print(f'{res_min:.10f} {res_max:.10f} {res_sum:.10f}')