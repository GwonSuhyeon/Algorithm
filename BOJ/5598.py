word = input()

translate = {}

for i in range(ord('A'), ord('Z') + 1):
    if i + 3 <= ord('Z'):
        translate[chr(i + 3)] = chr(i)
    else:
        translate[chr(ord('A') + (2 - (ord('Z') - i)))] = chr(i)

for i in word:
    print(translate[i], end='')