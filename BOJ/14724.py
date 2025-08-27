N = int(input())

arr = ['PROBRAIN', 'GROW', 'ARGOS', 'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY']

score = {}

for i in range(9):
    score[arr[i]] = max(map(int, input().split()))

print(max(score, key=score.get))