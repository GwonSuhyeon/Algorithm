N, M = map(int, input().split())

basket = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j, k = map(int, input().split())
    
    A = basket[:i - 1]
    B = basket[k - 1:j] + basket[i - 1:k - 1]
    C = basket[j:]
        
    basket = A + B + C

print(*basket)