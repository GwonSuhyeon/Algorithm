e, f, c = map(int, input().split())

res = 0
e += f

while e >= c:
    new = e // c
    res += new
    e = e % c + new

print(res)