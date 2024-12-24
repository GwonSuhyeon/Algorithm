n = int(input())
coded_msg = input().split()

decode_msg = ''
prev_word_len = 0

for word in coded_msg:
    if len(word) >= (prev_word_len + 1):
        print(word[prev_word_len], end='')
    else:
        print(' ', end='')
    
    prev_word_len = len(word) - 1