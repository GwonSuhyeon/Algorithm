n = int(input())

res = 0
money = 0

for _ in range(n):
    t = int(input())

    money += t
    
    res = min(money, res)

print(abs(res))