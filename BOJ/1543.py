s = input()
word = input()

idx = 0
res = 0

while idx < len(s):
    try:
        idx += (s[idx:].index(word) + len(word))
                
        res += 1
            
    except ValueError:
        break

print(res)