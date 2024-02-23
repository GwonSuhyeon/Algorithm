from collections import defaultdict
from collections import Counter

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
s = list(map(int, input().split()))


# ### DefaultDictionary 사용 948ms ###
# hashmap = defaultdict(int)

# for i in cards:
#     hashmap[i] += 1

# for i in s:
#     print(hashmap[i])



### Dictionary 사용 836ms ###
# hashmap = {}

# for i in cards:
#     if i not in hashmap:
#         hashmap[i] = 1
    
#     else:
#         hashmap[i] += 1

# for i in s:
#     if i in hashmap:
#         print(hashmap[i])
    
#     else:
#         print(0)


### Counter 사용 784ms ###
counter = Counter(cards)

for i in s:
    print(counter[i])