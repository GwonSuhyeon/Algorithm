from collections import defaultdict


res_p, res_t = 0, 0
solve = defaultdict(int)

while True:
    line = input()
    
    if line == '-1':
        break
    
    time, name, result = line.split()
    
    if result == 'wrong':
        solve[name] += 1
    else:
        if solve[name] > 0:
            res_t += int(time) + (solve[name] * 20)
        else:
            res_t += int(time)
        
        res_p += 1

print(res_p, res_t)