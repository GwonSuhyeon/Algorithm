res = 0
cnt = 0

while True:
    x = input()
    
    if cnt == 0:
        res = int(x)
    else:
        if x == '+':
            res += int(input())
        elif x == '-':
            res -= int(input())
        elif x == '*':
            res *= int(input())
        elif x == '/':
            res //= int(input())
        elif x == '=':
            break
    
    cnt += 1

print(res)