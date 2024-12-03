T = int(input())

lines = []

for _ in range(T):
    size = int(input())

    if size == 1:
        lines.append('#')
        lines.append('eof')
        continue

    for i in range(size):
        if i == 0:
            lines.append('#' * size + '\n')
            continue
        elif i == (size - 1):
            lines.append('#' * size)
            lines.append('eof')
            continue
        
        for k in range(size):
            if k == 0:
                lines.append('#')
            elif k == (size - 1):
                lines.append('#' + '\n')
            else:
                lines.append('J')

for idx, line in enumerate(lines):
    if 0 < idx == (len(lines) - 1):
        print()
    elif line == 'eof':
        print('\n')
    else:
        print(line, end='')