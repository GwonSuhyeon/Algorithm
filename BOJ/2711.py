T = int(input())

for _ in range(T):
    pos, word = input().split()
    
    print(word[:int(pos) - 1] + word[int(pos):])