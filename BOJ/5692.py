import sys


factorial = [1] * 6

for i in range(5):
    factorial[i + 1] = factorial[i] * (i + 1)

while True:
    line = sys.stdin.readline().rstrip()

    if line == '0':
        break
    
    res = 0

    for idx, ch in enumerate(line):
        digit = ord(ch) - ord('0')
        res += (digit * factorial[len(line) - idx])

    print(res)