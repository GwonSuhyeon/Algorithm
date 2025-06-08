C = int(input())

for _ in range(C):
    line = list(map(int, input().split()))
    
    N = line[0]
    
    score = line[1:]
    
    avg = sum(score) / len(score)
    
    res = [i for i in score if i > avg]
    
    print(f'{(len(res) / N) * 100:.3f}%')