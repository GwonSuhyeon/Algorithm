pre = float(input())

while True:
    current = float(input())
    
    if current == 999:
        break
    
    print("%.2f" % (current - pre))
    
    pre = current