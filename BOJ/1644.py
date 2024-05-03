N = int(input())

et = [0 for _ in range(4000001)]
et[1] = 1

for i in range(2, 4000001):
    if et[i] == 1:
        continue
    
    for k in range(i * 2, 4000001, i):
        et[k] = 1

prefixSum = []
prefixSum.append(0)

for i in range(1, 4000001):
    if et[i] == 0:
        if len(prefixSum) > 1:
            prefixSum.append(prefixSum[-1] + i)
        
        else:
            prefixSum.append(i)

front, back = 1, 1

res = 0

while True:
    if front > back or back == len(prefixSum):
        break
    
    num = prefixSum[back] - prefixSum[front - 1]
    
    if num == N:
        front += 1
        res += 1
    
    elif num > N:
        front += 1
    
    elif num < N:
        back += 1

print(res)