n = int(input())

for _ in range(n):
    arr1 = sorted(list(map(int, input().split())))
    arr2 = sorted(list(map(int, input().split())))

    if arr1[-1]**2 == (arr1[0]**2 + arr1[1]**2) and arr2[-1]**2 == (arr2[0]**2 + arr2[1]**2):
        if arr1[0] == arr2[0] and arr1[1] == arr2[1] and arr1[2] == arr2[2]:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')