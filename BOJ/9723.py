T = int(input())

for i in range(1, T + 1):
    abc = sorted(list(map(int, input().split())), reverse=True)

    if abc[0]**2 == abc[1]**2 + abc[2]**2:
        print(f'Case #{i}: YES')
    else:
        print(f'Case #{i}: NO')