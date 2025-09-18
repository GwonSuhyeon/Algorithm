while True:
    n = int(input())

    if n == 0:
        break
    
    res = 0

    words = []

    for _ in range(n):
        words.append(input())
    
    while True:
        empty = False

        for idx, word in enumerate(words):
            if len(word) == 1:
                empty = True

                break
            
            words[idx] = word[1:]
        
        if empty == True:
            break
        
        if len(set(words)) < n:
            break
        
        res += 1
    
    print(res)