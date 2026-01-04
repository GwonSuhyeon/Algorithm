n = int(input())

for _ in range(n):
    words = input().split()

    res = [word if len(word) != 4 else '****' for word in words]

    print(' '.join(res), end='\n\n')