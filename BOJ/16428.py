A, B = map(int, input().split())

q = A // B
r = A % B

if r < 0:
    r += abs(B)

    if B > 0:
        q -= 1
    else:
        q += 1

print(q)
print(r)
