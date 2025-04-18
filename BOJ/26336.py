t = int(input())

for _ in range(t):
    miles, gas, food = map(int, input().split())

    move = 0
    res = 0

    for i in range(1, miles):
        move = i

        if (move % gas == 0) or (move % food == 0):
            res += 1
    
    print(miles, gas, food)
    print(res)