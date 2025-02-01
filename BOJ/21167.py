import math


while True:
    try:
        R, S = map(float, input().split())

        V = math.sqrt((R * (S + 0.16)) / 0.067)

        print(int(round(V)))

    except:
        break