import math


while True:
    D, Resolution_H, Resolution_V = map(float, input().split())

    if D == 0 and Resolution_H == 0 and Resolution_V == 0:
        break

    W = (16 * D) / math.sqrt(337)
    H = (9 / 16) * W

    DPI_H = Resolution_H / W
    DPI_V = Resolution_V / H

    print(f'Horizontal DPI: {DPI_H:.2f}')
    print(f'Vertical DPI: {DPI_V:.2f}')