arr = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    S = input()
    
    res = 0
    
    if S == '#':
        break
    
    for s in S:
        if s in arr:
            res += 1
    
    print(res)