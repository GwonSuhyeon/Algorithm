s = int(input())

number = '0'
cnt = 0

while True:
    
    if '666' in number:
        cnt += 1
    
    if cnt == s:
        break
    
    number = str(int(number) + 1)

print(number)