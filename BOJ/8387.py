n = int(input())
line1 = input()
line2 = input()

res = 0

for a, b in zip(line1, line2):
    if a == b:
        res += 1

print(res)