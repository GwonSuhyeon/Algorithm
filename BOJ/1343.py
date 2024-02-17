s = list(input())

board = []

res = ''
temp = ''

for i in s:
    if i == 'X':
        temp += i
    
    else:
        if temp != '':
            board.append(temp)
            temp = ''
        
        board.append('.')

if temp != '':
    board.append(temp)

for i in board:
    if len(i) % 2 == 1 and i != '.':
        res = '-1'
        
        break

if res == '':
    for i in board:
        
        if 'X' in i:
            length = len(i)
            
            while length > 0:
                if length >= 4:
                    length -= 4
                    
                    res += 'AAAA'
                
                else:
                    length -= 2
                    
                    res += 'BB'

        else:
            res += '.'

print(res)