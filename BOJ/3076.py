R, C = map(int, input().split())
A, B = map(int, input().split())

for r in range(R):
    for _ in range(A):
        row = []
        
        for c in range(C):
            if (r + c) % 2 == 0:
                row.append('X' * B)
            else:
                row.append('.' * B)
        
        print(''.join(row))