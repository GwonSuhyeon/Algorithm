import math


D, H, W = map(int, input().split())

i = D / math.sqrt((H * H) + (W * W))

height = int(H * i)
width = int(W * i)

print(height, width)