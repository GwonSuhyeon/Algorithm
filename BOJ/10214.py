T = int(input())

for _ in range(T):
    Yonsei, Korea = 0, 0
    
    for _ in range(9):
        y, k = map(int, input().split())

        Yonsei += y
        Korea += k

    if Yonsei == Korea:
        print('Draw')
    elif Yonsei > Korea:
        print('Yonsei')
    elif Yonsei < Korea:
        print('Korea')