T = int(input())

for _ in range(T):
    score = sorted(list(map(int, input().split())))
    
    if abs(score[1] - score[3]) >= 4:
        print('KIN')
    else:
        print(sum(score[1:-1]))