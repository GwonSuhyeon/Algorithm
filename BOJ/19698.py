N, W, H, L = map(int, input().split())

res = min(N, (W // L) * (H // L))

print(res)