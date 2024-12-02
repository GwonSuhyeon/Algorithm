cost = {
    'Paper': 57.99,
    'Printer': 120.50,
    'Planners': 31.25,
    'Binders': 22.50,
    'Calendar': 10.95,
    'Notebooks': 11.20,
    'Ink': 66.95
}

res = 0

while True:
    item = input()

    if item == 'EOI':
        break
    
    res += cost[item]

print(f'${res:.2f}')