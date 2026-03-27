A = list(map(int, input().split()))
B = int(input())

res = 0

for a in A:
    if len(str(a)) > len(str(B)):
        if (a // (10**(len(str(a)) - len(str(B))))) == B:
            res += 1

print(res)