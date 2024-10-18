while True:
    total, conservative, reformist = map(int, input().split())

    other = total - (conservative + reformist)

    if total == 0 and conservative == 0 and reformist == 0:
        break
    
    if reformist >= total // 2 and conservative + other <= reformist:
        print(-1)
    elif conservative >= total // 2 and reformist + other < conservative:
        print(0)
    elif (total // 2 - conservative) <= (total - (conservative + reformist)):
        print(total // 2 - conservative + 1)