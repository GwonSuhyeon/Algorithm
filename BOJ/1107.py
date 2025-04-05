import sys


input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

plus_minus_cnt = abs(N - 100)

if M == 0:
    if abs(N - 100) <= len(str(N)):
        res = abs(N - 100)
    else:
        res = len(str(N))
elif N == 100:
    broken = set(map(int, input().rstrip().split()))
    res = 0
else:
    broken = set(map(int, input().rstrip().split()))

    up = N
    down = N

    diff_up = 999999999
    diff_down = 999999999

    while True:
        up_broken = False
        down_broken = False

        for digit in str(up):
            if int(digit) in broken:
                up_broken = True
                break
        
        for digit in str(down):
            if int(digit) in broken:
                down_broken = True
                break
            
        if up_broken == False or down_broken == False:
            if up_broken == False:
                diff_up = abs(N - up)
            
            if down_broken == False:
                diff_down = abs(N - down)
            
            res = min(diff_up + len(str(up)), diff_down + len(str(down)))
            
            break
        
        if up == 100 or down == 100:
            if up == 100:
                res = abs(N - up)
            
            if down == 100:
                res = abs(N - down)
            
            break
        
        if down > 0:
            down -= 1
        
        up += 1

res = min(plus_minus_cnt, res)

print(res)