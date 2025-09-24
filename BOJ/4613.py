value = {chr(i): (i - ord('A') + 1) for i in range(ord('A'), ord('Z') + 1)}

while True:
    line = input()

    if line == '#':
        break
    
    res = 0

    for idx, i in enumerate(line):
        if i != ' ':
            res += (idx + 1) * value[i]
    
    print(res)