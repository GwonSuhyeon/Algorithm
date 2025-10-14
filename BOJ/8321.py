n, k, s = map(int, input().split())
screws = sorted(list(map(int, input().split())), reverse=True)

res = 0
current_screws = 0

for i in screws:
    current_screws += i
    res += 1

    if current_screws >= (k * s):
        break

print(res)