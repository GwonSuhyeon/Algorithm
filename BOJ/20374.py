import sys


input = sys.stdin.readline

res = 0

while True:
    try:
        a, b = map(int, input().rstrip().split('.'))

        res += (a * 100) + b
    except:
        break

print(f'{res // 100}.{res % 100:02d}')