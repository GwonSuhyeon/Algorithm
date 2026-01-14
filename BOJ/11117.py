from collections import Counter


T = int(input())

for _ in range(T):
    box = Counter(input())
    W = int(input())

    for _ in range(W):
        word = Counter(input())

        res = 'YES'

        for key, value in word.items():
            if value > box[key]:
                res = 'NO'

                break
        
        print(res)