from collections import defaultdict


N = int(input())

if N == 0:
    print('divide by zero')
else:
    score = list(map(int, input().split()))

    avg = sum(score) / N
    p = 0

    temp = defaultdict(int)

    for num in score:
        temp[num] += 1
    
    for key, value in temp.items():
        p += key * (value / N)
    
    if p == 0:
        print('divide by zero')
    else:
        print(f'{avg / p:.2f}')