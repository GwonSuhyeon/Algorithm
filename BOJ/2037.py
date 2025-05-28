p, w = map(int, input().split())
s = input()

res = 0
press_cnt = 0
prev_key = ''

for i in s:
    if i in ['A', 'B', 'C']:
        keypad = ['A', 'B', 'C']
        key = 2
    
    elif i in ['D', 'E', 'F']:
        keypad = ['D', 'E', 'F']
        key = 3
    
    elif i in ['G', 'H', 'I']:
        keypad = ['G', 'H', 'I']
        key = 4
    
    elif i in ['J', 'K', 'L']:
        keypad = ['J', 'K', 'L']
        key = 5
    
    elif i in ['M', 'N', 'O']:
        keypad = ['M', 'N', 'O']
        key = 6
    
    elif i in ['P', 'Q', 'R', 'S']:
        keypad = ['P', 'Q', 'R', 'S']
        key = 7
    
    elif i in ['T', 'U', 'V']:
        keypad = ['T', 'U', 'V']
        key = 8
    
    elif i in ['W', 'X', 'Y', 'Z']:
        keypad = ['W', 'X', 'Y', 'Z']
        key = 9
    
    elif i == ' ':
        keypad = [' ']
        key = 1
    
    if prev_key == key and key != 1:
        res += w
    
    press_cnt = keypad.index(i) + 1
    
    res += press_cnt * p
    
    prev_key = key

print(res)