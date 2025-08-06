T = int(input())

for _ in range(T):
    line = input().split()
    
    if line[1] == '+':
        res = int(line[0]) + int(line[2])
    elif line[1] == '-':
        res = int(line[0]) - int(line[2])
    elif line[1] == '*':
        res = int(line[0]) * int(line[2])
    elif line[1] == '/':
        res = int(line[0]) // int(line[2])
    
    if res == int(line[-1]):
        print('correct')
    else:
        print('wrong answer')