T = int(input())

total = sum([i for i in range(ord('A'), ord('Z') + 1)])

for _ in range(T):
    S = input()
    
    ch = set()
    
    temp = 0
    
    for s in S:
        if s not in ch:
            ch.add(s)
            temp += ord(s)
    
    print(total - temp)