N = int(input())

score = {chr(i):i-64 for i in range(65, 91)}

for _ in range(N):
    line = ''.join(input().split())
    
    res = 0
    for i in line:
        res += score[i]
    
    if res == 100:
        print('PERFECT LIFE')
    else:
        print(res)