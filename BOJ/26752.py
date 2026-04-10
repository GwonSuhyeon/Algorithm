H, M, S = map(int, input().split())

total = (H * 3600) + (M * 60) + (S + 1)
total %= (24 * 3600)

print(f'{(total // 3600):02d}:{((total % 3600) // 60):02d}:{(total % 60):02d}')