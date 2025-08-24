T = int(input())

for _ in range(T):
    word1, word2 = input().split()
    
    res = []
    
    for w1, w2 in zip(word1, word2):
        distance = (ord(w2) - 64) - (ord(w1) - 64)
        
        if ord(w1) > ord(w2):
            distance += 26
        
        res.append(distance)
    
    print(f'Distances:', *res)