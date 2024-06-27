arr = {}

while True:
    city, temperature = input().split()
    
    arr[city] = int(temperature)
    
    if city == 'Waterloo':
        break

arr = sorted(arr.items(), key=lambda x : x[1])

print(arr[0][0])