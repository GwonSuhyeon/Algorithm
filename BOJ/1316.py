n = int(input())

res = 0

for _ in range(n):
    s = input()
    
    overlap = False
    
    for i in range(len(s) - 1):
        
        for k in range(i + 1, len(s)):
            if s[i] != s[k]:
                if s[i] in s[k:]:
                    overlap = True
                    
                    break
        
        if overlap == True:
            break
    
    if overlap == False:
        res += 1

print(res)