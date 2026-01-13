number = {chr(i): i - ord('a') for i in range(ord('a'), ord('z') + 1)}
decryption = {i - ord('a'): chr(i) for i in range(ord('a'), ord('z') + 1)}

n = int(input())
line = input().split()

for word in line:
    if len(word) % 2 != 0:
        word = word[:-1]
    
    for i in range(0, len(word), 2):
        y = number[word[i]]
        z = number[word[i + 1]]
        x = (y + z - n) % 26

        print(decryption[x], end='')
    
    print(' ', end='')