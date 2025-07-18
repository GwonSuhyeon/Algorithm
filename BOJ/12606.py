N = int(input())

for i in range(1, N + 1):
    words = input().split()
    
    print(f'Case #{i}: ', end='')
    print(*words[::-1])