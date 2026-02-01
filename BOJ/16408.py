cards = input().split()

res = []
rank = []

for card in cards:
    rank.append(card[0])

for i in set(rank):
    res.append(rank.count(i))

print(max(res))