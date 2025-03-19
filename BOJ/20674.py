n = int(input())

res = 0
yesterday = 0

for i in range(n):
    today = int(input())

    if i > 0:
        if today > yesterday:
            res += abs(yesterday - today)
        
        yesterday = min(yesterday, today)
    else:
        yesterday = today

print(res)