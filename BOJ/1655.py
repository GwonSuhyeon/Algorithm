import sys
import heapq


input = sys.stdin.readline

N = int(input())

max_heap = []
min_heap = []

for _ in range(N):
    value = int(input().rstrip())

    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-value, value))
    else:
        heapq.heappush(min_heap, value)
    
    if len(min_heap) == 0:
        print(max_heap[0][1])
    else:
        if max_heap[0][1] > min_heap[0]:
            a = heapq.heappop(max_heap)[1]
            b = heapq.heappop(min_heap)
            
            heapq.heappush(max_heap, (-b, b))
            heapq.heappush(min_heap, a)
        
        print(max_heap[0][1])