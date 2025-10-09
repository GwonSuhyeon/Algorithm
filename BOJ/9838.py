n = int(input())

gift = {}

for i in range(n):
    k = int(input())

    gift[i] = k

gift = sorted(gift.items(), key=lambda x : x[1])

for key, value in gift:
    print(key + 1)