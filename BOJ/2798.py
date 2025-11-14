N, M = map(int, input().split())
cards = sorted(list(map(int, input().split())), reverse=True)

res = 0

for i in range(len(cards) - 2):
    arr = []

    for k in range(i + 1, len(cards) - 1):
        for j in range(k + 1, len(cards)):
            if cards[i] + cards[k] + cards[j] <= M:
                res = max(res, cards[i] + cards[k] + cards[j])

print(res)