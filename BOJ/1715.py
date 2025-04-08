import heapq


N = int(input())

res = 0

min_heap = []

for _ in range(N):
    card_size = int(input())

    heapq.heappush(min_heap, card_size)

for _ in range(N - 1):    
    a = heapq.heappop(min_heap)
    b = heapq.heappop(min_heap)

    num = a + b

    res += num

    heapq.heappush(min_heap, num)

print(res)