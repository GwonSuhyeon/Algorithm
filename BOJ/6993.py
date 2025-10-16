T = int(input())

for _ in range(T):
    line = input().split()

    word = line[0]
    n = int(line[1])

    print(f'Shifting {word} by {n} positions gives us: {word[-n:]}{word[:-n]}')