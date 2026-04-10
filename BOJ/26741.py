X, Y = map(int, input().split())

B = (Y - (2 * X)) // 2
A = X - B

print(A, B)