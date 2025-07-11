N = int(input())

for _ in range(N):
    line = input()
    
    if 'P' in line:
        print('skipped')
    else:
        a, b = map(int, line.split('+'))
        
        print(a + b)