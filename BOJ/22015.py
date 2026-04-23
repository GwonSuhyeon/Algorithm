A, B, C = map(int, input().split())

maximum = max(A, B, C)

res = (maximum - A) + (maximum - B) + (maximum - C)

print(res)