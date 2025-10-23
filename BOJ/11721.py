line = input()

idx = 0

while idx < len(line):
    if idx + 10 < len(line):
        print(line[idx:idx+10])
    else:
        print(line[idx:])
    
    idx += 10