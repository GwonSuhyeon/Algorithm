lines = []
maximum = 0
res = ''

for _ in range(5):
    line = input()
    lines.append(line)
    maximum = max(maximum, len(line))

for i in range(maximum):
    for line in lines:
        if i < len(line):
            res += line[i]

print(res)