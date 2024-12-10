lines = []

while True:
    try:
        line = input()
    except:
        break
    
    line = line.replace('iiing', 'th')

    lines.append(line)

for line in lines:
    print(line)