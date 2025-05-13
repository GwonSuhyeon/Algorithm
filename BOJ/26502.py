n = int(input())

decoder = {'y': 'a', 'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'y',
            'Y': 'A', 'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'Y'}
replacement = decoder.values()

for _ in range(n):
    line = input()

    for ch in line:
        if ch in replacement:
            print(decoder[ch], end='')
        else:
            print(ch, end='')
            
    print()