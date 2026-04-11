line = input()

white = line.count('B')
black = line.count('C')

res = (white // 2) + (black // 2)

print(res)