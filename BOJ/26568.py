import re


n = int(input())

for idx in range(n):
    w = int(input())
    m = int(input())

    lines = []

    for _ in range(m):
        lines.append(input())
        
    text = ' '.join(lines)

    tokens = re.findall(r'\S+', text)
    gaps = re.split(r'\S+', text)

    if tokens:
        res = tokens[0]
        width = len(tokens[0])

        for i in range(1, len(tokens)):
            gap = gaps[i]
            word = tokens[i]

            if width + len(gap) + len(word) <= w:
                res += gap + word

                width += len(gap) + len(word)
            else:
                print(res)
                res = word

                width = len(word)

        print(res)

    if idx < n - 1:
        print()