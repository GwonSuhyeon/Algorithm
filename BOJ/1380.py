res = []

while True:
    n = int(input())
    
    if n == 0:
        break
    
    names = []
    numbers = []
    
    for _ in range(n):
        names.append(input())
        numbers.append(1)
    
    for _ in range((2*n) - 1):
        s = input().split()
        number = int(s[0])
        
        numbers[number - 1] -= 1
    
    idx = numbers.index(0)
    res.append(names[idx])
    
for i, name in enumerate(res):
    print(f'{i + 1} {name}')