N, S = input().split()

res = {}
answer = None

for _ in range(int(N)):
    name, text = input().split()

    if answer is not None:
        continue
    
    if name == S:
        answer = text
    else:
        res[name] = text

print(len([i for i in res.keys() if res[i] == answer]))