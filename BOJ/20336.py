n = int(input())

d = 0
dish = []

for _ in range(n):
    line = input().split()

    d = line[0]
    dish = line[1::]

print(d)

for i in dish:
    print(i)