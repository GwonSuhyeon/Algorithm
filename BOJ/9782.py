cnt = 0

while True:
    arr = list(map(int, input().split()))
    
    if arr[0] == 0:
        break
    
    cnt += 1
    
    if arr[0] % 2 == 0:
        print(f'Case {cnt}: {((arr[arr[0] // 2] + arr[(arr[0] // 2) + 1]) / 2):.1f}')
    else:
        print(f'Case {cnt}: {arr[(arr[0] + 1) // 2]:.1f}')