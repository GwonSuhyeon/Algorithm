n = int(input())

coordinate = []

for _ in range(n):
    coordinate.append(list(map(int, input().split())))

coordinate = sorted(coordinate)

for x, y in coordinate:
    print(f'{x} {y}')