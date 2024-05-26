N = int(input())

name = input()

score = {}

res = 0

for i in range(26):
    score[chr(ord('A') + i)] = i + 1

for i in name:
    res += score[i]

print(res)