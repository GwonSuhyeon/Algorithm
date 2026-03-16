t1, m1, t2, m2 = map(int, input().split())

start = (60 * t1) + m1
end = (60 * t2) + m2

if end < start:
    end += (60 * 24)

total = end - start

res = total // 30

print(total, res)