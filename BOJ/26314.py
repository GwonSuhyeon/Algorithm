n = int(input())

vowels = ['a', 'e', 'i', 'o', 'u']

for _ in range(n):
    name = input()

    vowel_cnt = 0

    for ch in name:
        if ch in vowels:
            vowel_cnt += 1
    
    if vowel_cnt > (len(name) - vowel_cnt):
        print(f'{name}\n{1}')
    else:
        print(f'{name}\n{0}')