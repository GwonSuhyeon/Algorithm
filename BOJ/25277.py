N = int(input())

S = input().split()

res = 0

for i in S:
    if i in ['he', 'she', 'him', 'her']:
        res += 1

print(res)