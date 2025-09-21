N = int(input())

for _ in range(N):
    words = input().split()

    print(*words[2:], words[0], words[1])