maximum = -1
row, col = 0, 0

for i in range(9):
    arr = list(map(int, input().split()))
    
    m = max(arr)
    
    if m > maximum:
        maximum = m
        col = arr.index(m) + 1
        row = i + 1

print(maximum)
print(row, col)