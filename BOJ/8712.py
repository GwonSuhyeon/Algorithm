n = int(input())

digit = 1

for i in range(n):
    row = [k for k in range(digit, digit + n)]
    
    digit += n

    if i % 2 == 1:
        row.reverse()
    
    print(*row)