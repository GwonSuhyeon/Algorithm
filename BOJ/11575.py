import sys


input = sys.stdin.readline

T = int(input().rstrip())

alphabet = {chr(i): idx for idx, i in enumerate(range(ord('A'), ord('Z') + 1))}
encrypt = {idx: chr(i) for idx, i in enumerate(range(ord('A'), ord('Z') + 1))}

for _ in range(T):
    a, b = map(int, input().rstrip().split())
    s = input().rstrip()

    res = []

    for i in s:
        res.append(encrypt[((a * alphabet[i]) + b) % 26])
    
    print(''.join(res))