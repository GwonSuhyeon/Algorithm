n = int(input())

names = []

for _ in range(n):
    s = input().split()
    
    names.append([int(s[0]), s[1]])

names = sorted(names, key=lambda x : x[0])

for age, name in names:
    print(f'{age} {name}')