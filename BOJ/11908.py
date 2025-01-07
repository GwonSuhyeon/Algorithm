n = int(input())

cards = sorted(list(map(int, input().split())))

print(sum(cards) - cards[-1])