T = int(input())

for _ in range(T):
    A = input()
    B = input()
    
    res = 0
    
    for a, b in zip(A, B):
        if a != b:
            res += 1
    
    print(f'Hamming distance is {res}.')