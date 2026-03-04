s = input()

interval = len(s) // 3

a = s[:interval]
b = s[interval:(interval * 2)]
c = s[(interval * 2):]

if a == b or a == c:
    print(a)
else:
    print(b)