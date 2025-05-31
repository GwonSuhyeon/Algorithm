while True:
    n = int(input())
    
    if n == 0:
        break
    
    words = []
    
    for _ in range(n):
        word = input()
        
        words.append([word.lower(), word])
    
    words = sorted(words, key=lambda x : x[0])
    
    print(words[0][1])