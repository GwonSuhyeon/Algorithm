N = int(input())
line = input()

Adrian = (['A', 'B', 'C'] * 34)[:100]
Bruno = ['B', 'A', 'B', 'C'] * 25
Goran = (['C', 'C', 'A', 'A', 'B', 'B'] * 17)[:100]

res = {'Adrian': 0, 'Bruno': 0, 'Goran': 0}

for idx, i in enumerate(line):
    if Adrian[idx] == i:
        res['Adrian'] += 1
    
    if Bruno[idx] == i:
        res['Bruno'] += 1
    
    if Goran[idx] == i:
        res['Goran'] += 1

names = [key for key, value in res.items() if value == max(res.values())]

print(res[names[0]])
for name in names:
    print(name)