import math

N, A, B, C, D = map(int, input().split())

X = math.floor(((N + A) - 1) / A) * B
Y = math.floor(((N + C) - 1) / C) * D

print(min(X, Y))