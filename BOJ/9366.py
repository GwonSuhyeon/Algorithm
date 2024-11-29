T = int(input())

for i in range(1, T + 1):
    arr = list(map(int, input().split()))

    if arr[0] + arr[1] <= arr[2]:
        res = 'invalid!'
    elif arr[0] + arr[2] <= arr[1]:
        res = 'invalid!'
    elif arr[1] + arr[2] <= arr[0]:
        res = 'invalid!'
    else:
        if len(set(arr)) == 3:
            res = 'scalene'
        elif len(set(arr)) == 2:
            res = 'isosceles'
        elif len(set(arr)) == 1:
            res = 'equilateral'
    
    print(f'Case #{i}: {res}')