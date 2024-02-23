n = int(input())
score = list(map(int, input().split()))

sum = 0
maximum = max(score)

for i in score:
    sum += ((i / maximum) * 100)

print('%.6f' % (sum / n))