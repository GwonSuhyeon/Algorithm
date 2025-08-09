res = 0

for r in range(8):
    line = input()
    
    for c, i in enumerate(line):
        if (r + c) % 2 == 0:
            if i == 'F':
                res += 1

print(res)  