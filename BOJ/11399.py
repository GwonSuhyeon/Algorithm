n = int(input())
s = sorted(map(int, input().split()))

sum = 0
res = 0

for i in s:
    sum += int(i)
    res += sum

print(res)