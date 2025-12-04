P = int(input())

for _ in range(P):
    line = input()

    arr = {
        'TTT': 0, 'TTH': 0, 'THT': 0, 'THH': 0, 'HTT': 0, 'HTH': 0, 'HHT': 0, 'HHH': 0
    }

    for i in range(len(line) - 2):
        sub = line[i:i+3]

        if sub in arr.keys():
            arr[sub] += 1
    
    print(*arr.values())