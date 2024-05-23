N = int(input())

for _ in range(N):
    s = input()
    
    s = s[:1].upper() + s[1:]
    
    print(s)