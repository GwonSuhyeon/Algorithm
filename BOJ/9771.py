word = input()

res = 0

while True:
    try:
        line = input()
        
        words = line.split()
        
        for w in words:
            if word in w:
                res += 1
    except:
        break

print(res)