T = int(input())

for i in range(T):
    country = input()
    
    if country[-1] == 'y':
        res = 'nobody'
    elif country[-1] in ['a', 'e', 'i', 'o', 'u']:
        res = 'a queen'
    else:
        res = 'a king'
    
    print(f'Case #{i + 1}: {country} is ruled by {res}.')