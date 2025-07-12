N = int(input())

for i in range(N):
    words = input().split()
    
    res = ' '.join(words[::-1])
    
    print(f'Case #{i + 1}: {res}')