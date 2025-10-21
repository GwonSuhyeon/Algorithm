n = int(input())

rect_x1 = 0
rect_y1 = 0
rect_x2 = 10000
rect_y2 = 10000

for _ in range(n):
    x1, x2, y1, y2 = map(int, input().split())

    rect_x1 = max(rect_x1, x1)
    rect_x2 = min(rect_x2, x2)
    rect_y1 = max(rect_y1, y1)
    rect_y2 = min(rect_y2, y2)

print(max(0, rect_x2 - rect_x1) * max(0, rect_y2 - rect_y1))