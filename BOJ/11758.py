import sys


input = sys.stdin.readline

x1, y1 = map(int, input().rstrip().split())
x2, y2 = map(int, input().rstrip().split())
x3, y3 = map(int, input().rstrip().split())

angle = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)

if angle > 0:
    print('1')

elif angle < 0:
    print('-1')

elif angle == 0:
    print(0)