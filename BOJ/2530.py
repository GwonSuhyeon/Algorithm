A, B, C = map(int, input().split())
D = int(input())

time = ((A * 3600) + (B * 60) + C + D) % (24 * 3600)

print(time // 3600, (time % 3600) // 60, time % 60)