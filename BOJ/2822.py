score = {}

for i in range(8):
    score[i + 1] = int(input())

score = sorted(score.items(), key=lambda x: -x[1])

print(sum([x[1] for x in score[:5]]))

score = sorted(score[:5], key=lambda x: x[0])

for i in range(5):
    print(score[i][0], end=' ')